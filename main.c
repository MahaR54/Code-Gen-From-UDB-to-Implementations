#include <stdio.h>
#include "inst_data.h"

int main() {
    printf("name: %s\n", INST_NAME);
    printf("encoding:\n");
    printf("  match: %s\n", MATCH_PATTERN);
    printf("  variables:\n");

    printf("    - name: xs2\n");
    printf("      location: %s\n", XS2_LOCATION);
    printf("    - name: xs1\n");
    printf("      location: %s\n", XS1_LOCATION);
    printf("    - name: xd\n");
    printf("      location: %s\n", XD_LOCATION);

    return 0;
}
