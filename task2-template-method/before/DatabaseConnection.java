import java.util.Date;
import java.util.List;

public interface DatabaseConnection {
    <T> List<T> query(String sql, Date from, Date to);
}
