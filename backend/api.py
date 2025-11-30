"""
Backend API module for Entangled with the Word.
Provides data access layer and AI-enhanced features.
"""
import os
from datetime import datetime
from typing import Optional
import pandas as pd


class DataStore:
    """Base class for CSV-based data storage."""
    
    def __init__(self, filepath: str, columns: list[str]):
        self.filepath = filepath
        self.columns = columns
        self._ensure_directory()
    
    def _ensure_directory(self) -> None:
        """Ensure the directory exists for the data file."""
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
    
    def read(self) -> pd.DataFrame:
        """Read data from CSV file."""
        if not os.path.exists(self.filepath):
            return pd.DataFrame(columns=self.columns)
        try:
            df = pd.read_csv(self.filepath)
            # Ensure all expected columns exist
            for col in self.columns:
                if col not in df.columns:
                    df[col] = "" if col not in ["count", "candles"] else 0
            return df
        except (pd.errors.EmptyDataError, Exception):
            return pd.DataFrame(columns=self.columns)
    
    def write(self, df: pd.DataFrame) -> bool:
        """Write data to CSV file."""
        try:
            df.to_csv(self.filepath, index=False)
            return True
        except Exception:
            return False
    
    def append(self, data: dict) -> bool:
        """Append a single row to the data file."""
        try:
            df = self.read()
            new_row = pd.DataFrame([data])
            df = pd.concat([df, new_row], ignore_index=True)
            return self.write(df)
        except Exception:
            return False


class ParablesAPI:
    """API for managing parables (suggestions and approved)."""
    
    SUGGEST_FILE = os.path.join("data", "suggested_parables.csv")
    APPROVED_FILE = os.path.join("gospel", "approved_parables.csv")
    COLUMNS = ["timestamp", "suggestion", "tag"]
    
    def __init__(self):
        self.suggestions_store = DataStore(self.SUGGEST_FILE, self.COLUMNS)
        self.approved_store = DataStore(self.APPROVED_FILE, self.COLUMNS)
    
    def get_suggestions(self) -> pd.DataFrame:
        """Get all pending suggestions."""
        return self.suggestions_store.read()
    
    def get_approved(self) -> pd.DataFrame:
        """Get all approved parables."""
        df = self.approved_store.read()
        if not df.empty and "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.sort_values("timestamp")
        return df
    
    def get_approved_by_category(self, category: str) -> pd.DataFrame:
        """Get approved parables filtered by category."""
        df = self.get_approved()
        if category and category != "All":
            df = df[df["tag"] == category]
        return df
    
    def submit_suggestion(self, suggestion: str, tag: str) -> bool:
        """Submit a new parable suggestion."""
        if not suggestion or not suggestion.strip():
            return False
        data = {
            "timestamp": datetime.now().isoformat(),
            "suggestion": suggestion.strip(),
            "tag": tag
        }
        return self.suggestions_store.append(data)
    
    def approve_suggestion(self, index: int) -> bool:
        """Move a suggestion from pending to approved."""
        suggestions = self.suggestions_store.read()
        if suggestions.empty or index >= len(suggestions):
            return False
        
        try:
            row = suggestions.iloc[index].to_dict()
            approved = self.approved_store.read()
            approved = pd.concat([approved, pd.DataFrame([row])], ignore_index=True)
            
            if not self.approved_store.write(approved):
                return False
            
            suggestions = suggestions.drop(index).reset_index(drop=True)
            return self.suggestions_store.write(suggestions)
        except Exception:
            return False
    
    def delete_suggestion(self, index: int) -> bool:
        """Delete a pending suggestion."""
        suggestions = self.suggestions_store.read()
        if suggestions.empty or index >= len(suggestions):
            return False
        
        try:
            suggestions = suggestions.drop(index).reset_index(drop=True)
            return self.suggestions_store.write(suggestions)
        except Exception:
            return False


class CommunionAPI:
    """API for managing communion reflections and candles."""
    
    REFLECTIONS_FILE = os.path.join("data", "communion_reflections.csv")
    CANDLES_FILE = os.path.join("data", "communion_candles.csv")
    REFLECTION_COLUMNS = ["timestamp", "entry"]
    CANDLE_COLUMNS = ["entry_index", "count"]
    
    def __init__(self):
        self.reflections_store = DataStore(self.REFLECTIONS_FILE, self.REFLECTION_COLUMNS)
        self.candles_store = DataStore(self.CANDLES_FILE, self.CANDLE_COLUMNS)
    
    def get_reflections(self) -> pd.DataFrame:
        """Get all reflections with candle counts."""
        reflections = self.reflections_store.read()
        if reflections.empty:
            return reflections
        
        reflections["timestamp"] = pd.to_datetime(reflections["timestamp"], errors="coerce")
        reflections = reflections.reset_index(drop=True)
        reflections["id"] = reflections.index
        
        candles = self.candles_store.read()
        if not candles.empty:
            candles["entry_index"] = candles["entry_index"].astype(int)
            candles["count"] = candles["count"].astype(int)
            candles = candles.rename(columns={"entry_index": "id"})
            reflections = pd.merge(reflections, candles, on="id", how="left")
            reflections["count"] = reflections["count"].fillna(0).astype(int)
        else:
            reflections["count"] = 0
        
        return reflections
    
    def get_top_reflections(self, date: Optional[datetime] = None, limit: int = 3) -> pd.DataFrame:
        """Get top reflections by candle count for a specific date."""
        reflections = self.get_reflections()
        if reflections.empty:
            return reflections
        
        if date:
            reflections = reflections[reflections["timestamp"].dt.date == date.date()]
        
        return reflections.sort_values(by="count", ascending=False).head(limit)
    
    def submit_reflection(self, entry: str) -> bool:
        """Submit a new reflection."""
        if not entry or not entry.strip():
            return False
        data = {
            "timestamp": datetime.now().isoformat(),
            "entry": entry.strip()
        }
        return self.reflections_store.append(data)
    
    def add_candle(self, entry_index: int) -> bool:
        """Add a candle (light) to a reflection."""
        candles = self.candles_store.read()
        
        if not candles.empty:
            candles["entry_index"] = candles["entry_index"].astype(int)
            candles["count"] = candles["count"].astype(int)
        
        if entry_index in candles["entry_index"].values:
            candles.loc[candles["entry_index"] == entry_index, "count"] += 1
        else:
            new_row = pd.DataFrame([[entry_index, 1]], columns=self.CANDLE_COLUMNS)
            candles = pd.concat([candles, new_row], ignore_index=True)
        
        return self.candles_store.write(candles)


class OpenAIService:
    """Service for AI-enhanced features using OpenAI."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client = None
    
    @property
    def client(self):
        """Lazy initialization of OpenAI client."""
        if self._client is None and self.api_key:
            try:
                import openai
                self._client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                pass
        return self._client
    
    @property
    def is_available(self) -> bool:
        """Check if OpenAI service is available."""
        return self.client is not None
    
    def enhance_reflection(self, reflection: str) -> Optional[str]:
        """Enhance a reflection with AI-generated spiritual insight."""
        if not self.is_available or not reflection:
            return None
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a spiritual guide who enhances reflections with poetic, quantum-spiritual insights. Keep responses brief and meaningful."
                    },
                    {
                        "role": "user",
                        "content": f"Enhance this spiritual reflection with a brief, poetic insight: {reflection}"
                    }
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception:
            return None
    
    def generate_parable_insight(self, parable: str) -> Optional[str]:
        """Generate insight for a parable using AI."""
        if not self.is_available or not parable:
            return None
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a quantum-spiritual interpreter who bridges ancient wisdom with modern understanding. Provide brief, meaningful insights."
                    },
                    {
                        "role": "user",
                        "content": f"Provide a brief quantum-spiritual insight for this parable: {parable}"
                    }
                ],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception:
            return None
