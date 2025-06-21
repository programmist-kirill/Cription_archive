#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Проверка аргументов с человеко-читаемыми сообщениями
    if (argc != 3) {
        fprintf(stderr, "Ошибка: Неверное количество аргументов\n");
        fprintf(stderr, "Использование: %s FILE_PATH TEXT_TO_WRITE\n", argv[0]);
        fprintf(stderr, "Пример: %s output.txt 'Привет, мир!'\n", argv[0]);
        return 1;
    }

    const char *filepath = argv[1];
    const char *text = argv[2];

    FILE *file = fopen(filepath, "w");
    if (!file) {
        perror("🚨 Ошибка открытия файла");
        return 2;
    }

    if (fprintf(file, "%s\n", text) < 0) {
        perror("🚨 Ошибка записи в файл");
        fclose(file);
        return 3;
    }

    fclose(file);
    printf("✅ Успешно записано в '%s'\n", filepath);
    return 0;
}