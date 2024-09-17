#include <stdio.h>
#include <string.h>

void Encrypt(char* text, char* result) {
    char key[] = "telkom1";
    int keyLen = strlen(key);
    int textLen = strlen(text);
    
    for (int i = 0; i < textLen; ++i) {
        result[i] = text[i] ^ key[i % keyLen];
    }
    result[textLen] = '\0';
}

int main() {
    printf("Moklet-sec Flag Checker\n");

    char userInp[256];
    printf("Masukkan flag >> ");
    fgets(userInp, sizeof(userInp), stdin);

    size_t len = strlen(userInp);
    if (len > 0 && userInp[len - 1] == '\n') {
        userInp[len - 1] = '\0';
    }

    char flagEnc[] = "\x39\x2a\x27\x27\x2a\x39\x4a\x26\x56\x1a\x58\x1d\x58\x02\x2b\x55\x3e\x34\x2c\x1f\x48\x24\x11\x5c\x54\x12";
    char encryptedInp[256];

    Encrypt(userInp, encryptedInp);

    if (strcmp(encryptedInp, flagEnc) == 0) {
        printf("Flag benar\n");
    } else {
        printf("Flag salah\n");
    }

    return 0;
}
