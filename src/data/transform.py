
import re
import pandas as pd

def process_raw_todoist_data(raw_csv_path):
    df = pd.read_csv(raw_csv_path)

    def extract_labels_and_clean(content):
        labels = re.findall(r'@[\w:\\-]+', content)
        clean_labels = [re.sub(r'[^\w]', '_', label.strip('@')) for label in labels]
        return labels, clean_labels

    unique_clean_labels = set()
    for content in df['CONTENT'].astype(str):
        _, clean_labels = extract_labels_and_clean(content)
        unique_clean_labels.update(clean_labels)

    for clean_label in unique_clean_labels:
        df[clean_label] = df['CONTENT'].astype(str).apply(
            lambda x: clean_label in re.sub(r'[^\w]', '_', x)
        )

    df['STRIPPED_CONTENT'] = df['CONTENT'].astype(str).apply(
        lambda x: re.sub(r'@[\w:\\-]+\s*', '', x).strip()
    )
    return df