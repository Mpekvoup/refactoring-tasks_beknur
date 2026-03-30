import java.util.Objects;

/**
 * Value Object для адреса сотрудника.
 * Immutable класс - все поля final, без сеттеров.
 */
public final class Address {
    private final String streetAddress;
    private final String city;
    private final String zipCode;
    private final String country;

    /**
     * Конструктор адреса.
     * @param streetAddress улица
     * @param city город
     * @param zipCode почтовый индекс
     * @param country страна
     */
    public Address(String streetAddress, String city, String zipCode, String country) {
        if (streetAddress == null || city == null || zipCode == null || country == null) {
            throw new IllegalArgumentException("All address fields must be non-null");
        }
        this.streetAddress = streetAddress;
        this.city = city;
        this.zipCode = zipCode;
        this.country = country;
    }

    /**
     * Возвращает полный адрес в виде строки.
     * @return отформатированный адрес
     */
    public String getFullAddress() {
        return streetAddress + ", " + city + ", " + zipCode + ", " + country;
    }

    public String getStreetAddress() { return streetAddress; }
    public String getCity() { return city; }
    public String getZipCode() { return zipCode; }
    public String getCountry() { return country; }

    @Override
    public String toString() {
        return getFullAddress();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Address address = (Address) o;
        return Objects.equals(streetAddress, address.streetAddress) &&
               Objects.equals(city, address.city) &&
               Objects.equals(zipCode, address.zipCode) &&
               Objects.equals(country, address.country);
    }

    @Override
    public int hashCode() {
        return Objects.hash(streetAddress, city, zipCode, country);
    }
}
