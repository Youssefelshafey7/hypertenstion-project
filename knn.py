import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# ======================== LOAD DATA ========================
df = pd.read_csv("hypertension_dataset.csv")

df_encoded = df.copy()
encoders = {}

# Encode categorical columns
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    encoders[col] = le

# Split data
X = df_encoded.drop("Has_Hypertension", axis=1)
y = df_encoded["Has_Hypertension"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale for KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# ======================== TRAIN KNN ========================
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

# ======================== FUNCTIONS FOR GUI ========================
def predict_knn(scaled_input_df):
    return knn_model.predict(scaled_input_df)[0]

def get_scaler():
    return scaler

def get_encoders():
    return encoders
