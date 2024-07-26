import os
from ebooklib import epub
from datetime import datetime

def replace_umlauts(text):
    """
    Ersetzt Umlaute in einem Text durch ae, oe, ue, Ae, Oe, Ue und ss.

    Args:
        text (str): Der ursprüngliche Text.

    Returns:
        str: Der Text mit ersetzten Umlauten.
    """
    replacements = {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
        'Ä': 'Ae',
        'Ö': 'Oe',
        'Ü': 'Ue',
        'ß': 'ss'
    }
    for umlaut, replacement in replacements.items():
        text = text.replace(umlaut, replacement)
    return text

def format_date(date_str):
    """
    Formatiert ein Datum in das Format YYYYMMDD.

    Args:
        date_str (str): Das ursprüngliche Datum.

    Returns:
        str: Das formatierte Datum.
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime("%Y")
    except ValueError:
        return "unknown_date"

def get_metadata(book, field):
    """
    Holt Metadaten aus dem Buch und gibt einen Standardwert zurück, wenn das Feld fehlt.

    Args:
        book (epub.EpubBook): Das EPUB-Buch.
        field (str): Das Metadatenfeld.

    Returns:
        str: Der Wert des Metadatenfelds oder ein Standardwert.
    """
    try:
        return book.get_metadata("DC", field)[0][0]
    except IndexError:
        return "unknown"

def rename_epub_files(directory):
    """
    Benennt EPUB-Dateien im angegebenen Verzeichnis basierend auf ihren Metadaten um.

    Args:
        directory (str): Der Verzeichnispfad, in dem sich die EPUB-Dateien befinden.

    Returns:
        None
    """
    for filename in os.listdir(directory):
        if filename.endswith(".epub"):
            filepath = os.path.join(directory, filename)
            print(f"Bearbeite Datei: {filename}")
            book = epub.read_epub(filepath)
            author = get_metadata(book, "creator")
            title = get_metadata(book, "title")
            date = get_metadata(book, "date")
            formatted_date = format_date(date)
            if formatted_date != "unknown_date":
                new_filename = f"{formatted_date}_{replace_umlauts(author)}_{replace_umlauts(title)}.epub"
            else:
                new_filename = f"{replace_umlauts(author)}_{replace_umlauts(title)}.epub"
            new_filepath = os.path.join(directory, new_filename)
            os.rename(filepath, new_filepath)
            print(f"Umbenannt in: {new_filename}")

rename_epub_files(os.path.dirname(os.path.abspath(__file__)))