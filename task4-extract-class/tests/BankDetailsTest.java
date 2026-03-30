import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Тесты для класса BankDetails.
 */
public class BankDetailsTest {

    @Test
    public void testBankDetailsCreation() {
        BankDetails bank = new BankDetails("Chase Bank", "12345678", "123456789");
        assertEquals("Chase Bank", bank.getBankName());
        assertEquals("12345678", bank.getAccountNumber());
        assertEquals("123456789", bank.getRoutingNumber());
    }

    @Test
    public void testValidBankAccount() {
        BankDetails bank = new BankDetails("Chase Bank", "12345678", "123456789");
        assertTrue(bank.validate());
    }

    @Test
    public void testInvalidAccountNumber_TooShort() {
        BankDetails bank = new BankDetails("Chase Bank", "1234567", "123456789");
        assertFalse(bank.validate());
    }

    @Test
    public void testInvalidRoutingNumber_WrongLength() {
        BankDetails bank = new BankDetails("Chase Bank", "12345678", "12345678");
        assertFalse(bank.validate());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullBankNameThrowsException() {
        new BankDetails(null, "12345678", "123456789");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullAccountNumberThrowsException() {
        new BankDetails("Chase Bank", null, "123456789");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullRoutingNumberThrowsException() {
        new BankDetails("Chase Bank", "12345678", null);
    }

    @Test
    public void testBankDetailsEquality() {
        BankDetails bank1 = new BankDetails("Chase Bank", "12345678", "123456789");
        BankDetails bank2 = new BankDetails("Chase Bank", "12345678", "123456789");
        BankDetails bank3 = new BankDetails("Wells Fargo", "87654321", "987654321");

        assertEquals(bank1, bank2);
        assertNotEquals(bank1, bank3);
    }

    @Test
    public void testBankDetailsHashCode() {
        BankDetails bank1 = new BankDetails("Chase Bank", "12345678", "123456789");
        BankDetails bank2 = new BankDetails("Chase Bank", "12345678", "123456789");

        assertEquals(bank1.hashCode(), bank2.hashCode());
    }

    @Test
    public void testBankDetailsToString() {
        BankDetails bank = new BankDetails("Chase Bank", "12345678", "123456789");
        assertEquals("Bank: Chase Bank, Account: 12345678, Routing: 123456789", bank.toString());
    }
}
