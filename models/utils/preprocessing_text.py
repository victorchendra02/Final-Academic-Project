# import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
class GeneralNLPPreprocessing:
    
    def remove_punctuation(self, text):
        # import string

        punctuations = string.punctuation  # !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        no_punct = "".join([char for char in text if char not in punctuations])
        return no_punct

    def remove_stopwords(self, text):
        # import nltk
        # from nltk.corpus import stopwords
        # nltk.download('stopwords')

        stop_words = stopwords.words('english')  # Get English stopwords
        words = text.split()  # Convert text to lowercase and split into words
        filtered_words = [word for word in words if word.lower() not in stop_words]  # Filter out stop words
        return " ".join(filtered_words)

    def lowercase(self, text):
        return text.lower()

    def stemming(self, text):
        # import nltk
        # from nltk.stem import PorterStemmer
        # nltk.download('punkt')

        stemmer = PorterStemmer()
        words = text.split()
        stemmed_words = [stemmer.stem(word, to_lowercase=False) for word in words]  # Apply stemming to each word
        return " ".join(stemmed_words)

    def lemmatize(self, text):
        import nltk
        from nltk.stem import WordNetLemmatizer
        from nltk.corpus import wordnet

        def get_wordnet_pos(treebank_tag):
            """
            Convert the part-of-speech naming scheme from Penn Treebank to WordNet.
            """
            if treebank_tag.startswith('J'):
                return wordnet.ADJ
            elif treebank_tag.startswith('V'):
                return wordnet.VERB
            elif treebank_tag.startswith('N'):
                return wordnet.NOUN
            elif treebank_tag.startswith('R'):
                return wordnet.ADV
            else:
                return wordnet.NOUN  # Default to noun if not found
        """
        Perform lemmatization on the input text.
        """
        lemmatizer = WordNetLemmatizer()
        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)
        lemmatized_words = []
        for word, tag in pos_tags:
            pos = get_wordnet_pos(tag)
            lemmatized_word = lemmatizer.lemmatize(word, pos=pos)
            lemmatized_words.append(lemmatized_word)
        return ' '.join(lemmatized_words)

    def fit(self, text):
        # text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        # text = self.lowercase(text)
        text = self.stemming(text)
        # text = self.lemmatize(text)

        return text


import re
import html
import unicodedata
from bs4 import BeautifulSoup
class Preprocess:

    def decode_html_entities(self, text: str):
        """
        Decode HTML entities in a given text. Example:
            - &amp; --> &
            - &lt; --> <
            - &gt; --> >
            - &quot; --> "
            - &apos; --> '
            - etc.
        """
        # import html

        decoded_text = html.unescape(text)
        return str(decoded_text)

    def remove_html_tag_in_a_text(self, text: str):
        """
        Remove html tag in a text such as:
            - <br>
            - <span></span>
            - <b></b>
            - etc.
        """
        # from bs4 import BeautifulSoup

        clean_text = BeautifulSoup(text, 'html.parser').get_text()
        return str(clean_text)

    def remove_accented_characters(self, text: str):
        """
        Function replaces accented characters with their closest ASCII equivalents.
        In some cases, this may not be the desired behavior.
        For example, the character "ñ" would be replaced with "n".

        ÀáÉéÍíÓóÚúÑñ --> AaEeIiOoUuNn
        """
        # import unicodedata

        new_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return str(new_text)

    def remove_redundant_white_spaces(self, text: str):
        # import re

        clean_text = re.sub(r'\s+', ' ', text).strip()
        return str(clean_text)

    def replace_img_tag_with_the_alt_attribute(self, html_text: str):
        """
        Before using this function, must perform:
            - `decode_html_entities()`
        """
        # from bs4 import BeautifulSoup

        soup = BeautifulSoup(html_text, 'html.parser')
        img_tags = soup.find_all('img')

        # Replace img tags with their alt attribute content
        for img_tag in img_tags:
            alt_text = img_tag.get('alt', '[MISSING_ALT]')  # Get alt attribute or [MISSING_ALT] string if missing
            img_tag.replace_with(alt_text)

        modified_text = str(soup)

        return modified_text

    def clean_text(self, text: str):
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
        text = text.replace("\r", " ")
        text = text.replace("\v", " ")
        return text

    def findall_occurrences_of_LaTex(self, text: str) -> list:
        """
        Find/capture all occurrences LaTex that indicated with `$ ... $` with an n number of `$`
        """
        # import re

        regex = re.compile(r'(\$+.*?\$+)')
        matches = re.findall(regex, text)  # Output: [$...$, $...$, ...]

        return matches

    def extract_inside_dollar_sign(self, text: str) -> str:
        """
        This function only for this specific input:
            - `$ 1/x \leq 10 $`  -->  ` 1/x \leq 10 `
            - `$1  anything z$`  -->  `1   anything z`  with the redundant spaces

        You can say this function remove suffix and prefix for `$` sign\n
        OR\n
        It takes/extracts text that flanked (diapit) with `$` sign
        """
        # import re

        regex = re.compile(r'\$+(.*?)\$+')
        result = re.findall(regex, text)
        return result[0]

    def fit(self, text: str):
        text = self.decode_html_entities(text)
        text = self.remove_accented_characters(text)
        text = self.clean_text(text)
        text = self.remove_redundant_white_spaces(text)
        text = self.replace_img_tag_with_the_alt_attribute(text)

        text = self.remove_html_tag_in_a_text(text)
        text = self.remove_redundant_white_spaces(text)

        text = text.replace("\[", "$")
        text = text.replace("\]", "$")

        captured_LaTex = self.findall_occurrences_of_LaTex(text)
        processed_LaTex = captured_LaTex.copy()
        for i in range(len(processed_LaTex)):
            processed_LaTex[i] = self.extract_inside_dollar_sign(processed_LaTex[i])

        for j in range(len(captured_LaTex)):
            text = text.replace(captured_LaTex[j], processed_LaTex[j])

        # text = GeneralNLPPreprocessing().fit(text)
        text = text.replace("\\", " ")
        text = self.remove_redundant_white_spaces(text)
        return text
