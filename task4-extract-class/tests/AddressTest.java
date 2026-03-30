import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Тесты для класса Address.
 */
public class AddressTest {

    @Test
    public void testAddressCreation() {
        Address address = new Address("123 Main St", "New York", "10001", "USA");
        assertEquals("123 Main St", address.getStreetAddress());
        assertEquals("New York", address.getCity());
        assertEquals("10001", address.getZipCode());
        assertEquals("USA", address.getCountry());
    }

    @Test
    public void testGetFullAddress() {
        Address address = new Address("123 Main St", "New York", "10001", "USA");
        assertEquals("123 Main St, New York, 10001, USA", address.getFullAddress());
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullStreetThrowsException() {
        new Address(null, "New York", "10001", "USA");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testNullCityThrowsException() {
        new Address("123 Main St", null, "10001", "USA");
    }

    @Test
    public void testAddressEquality() {
        Address address1 = new Address("123 Main St", "New York", "10001", "USA");
        Address address2 = new Address("123 Main St", "New York", "10001", "USA");
        Address address3 = new Address("456 Oak Ave", "Boston", "02101", "USA");

        assertEquals(address1, address2);
        assertNotEquals(address1, address3);
    }

    @Test
    public void testAddressHashCode() {
        Address address1 = new Address("123 Main St", "New York", "10001", "USA");
        Address address2 = new Address("123 Main St", "New York", "10001", "USA");

        assertEquals(address1.hashCode(), address2.hashCode());
    }

    @Test
    public void testAddressToString() {
        Address address = new Address("123 Main St", "New York", "10001", "USA");
        assertEquals("123 Main St, New York, 10001, USA", address.toString());
    }

    @Test
    public void testAddressImmutability() {
        Address address = new Address("123 Main St", "New York", "10001", "USA");
        String originalFull = address.getFullAddress();

        // Попытка изменить возвращенные значения не должна влиять на объект
        String city = address.getCity();
        city = "Boston";  // не влияет на address

        assertEquals(originalFull, address.getFullAddress());
    }
}
