import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# ======================== LOAD & PREPARE DATA ========================
df = pd.read_csv("hypertension_dataset.csv")

df_encoded = df.copy()
encoders = {}

# Encode categorical columns
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    encoders[col] = le

# Train-test split
X = df_encoded.drop("Has_Hypertension", axis=1)
y = df_encoded["Has_Hypertension"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================== TRAIN RANDOM FOREST ========================
rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)

# ======================== FUNCTIONS FOR GUI ========================
def predict_rf(input_df):
    """
    Accepts a dataframe with SAME columns as training data.
    Returns the prediction (0 or 1).
    """
    return rf_model.predict(input_df)[0]

def get_encoders():
    """Return encoders so GUI can encode new data."""
    return encoders
