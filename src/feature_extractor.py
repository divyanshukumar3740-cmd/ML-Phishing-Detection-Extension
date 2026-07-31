import urllib.parse
import re

class PhishingFeatureExtractor:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urllib.parse.urlparse(url)
        self.domain = self.parsed_url.netloc
        # Initializing with 0 to prevent missing key errors later.
        self.features = {}

    def extract_lexical_features(self):
        """
        Extracts features strictly from the URL string. 
        (Completed by Member 1)
        """
        # 1. URLLength & DomainLength
        self.features['URLLength'] = len(self.url)
        self.features['DomainLength'] = len(self.domain)
        
        # 2. IsHTTPS
        self.features['IsHTTPS'] = 1 if self.parsed_url.scheme == 'https' else 0
        
        # 3. IsDomainIP
        # Checks if the domain is a raw IPv4 address instead of a string name
        ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        self.features['IsDomainIP'] = 1 if ip_pattern.match(self.domain) else 0
        
        # 4. NoOfSubDomain
        # Rough calculation by counting dots in the domain name
        if self.features['IsDomainIP'] == 1:
            self.features['NoOfSubDomain'] = 0
        else:
            self.features['NoOfSubDomain'] = max(0, self.domain.count('.') - 1)

        # 5. Character Counts in URL
        self.features['NoOfEqualsInURL'] = self.url.count('=')
        self.features['NoOfQMarkInURL'] = self.url.count('?')
        self.features['NoOfAmpersandInURL'] = self.url.count('&')
        
        print("Lexical features extracted successfully.")

    def extract_dom_features(self, html_content):
        """
        Extracts features from the webpage source code.
        (TODO: Handoff to Member 2)
        """
        pass

    def get_features(self):
        """Returns the final dictionary to be fed into the ML model."""
        return self.features

# Quick Test to Ensure it Works
if __name__ == "__main__":
    test_url = "https://www.secure-login.bank-update.com/auth?user=123&token=abc"
    
    extractor = PhishingFeatureExtractor(test_url)
    extractor.extract_lexical_features()
    
    print("\nExtracted Features so far:")
    for key, value in extractor.get_features().items():
        print(f"{key}: {value}")