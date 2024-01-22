import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestHello {

    @Test
    public void testFoo() {
        int result = 5 + 5 * 2;
        assertEquals(result, 13);
    }

}