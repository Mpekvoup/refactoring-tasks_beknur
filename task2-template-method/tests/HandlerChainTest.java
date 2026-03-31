import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Тесты для цепочки обработчиков (Chain of Responsibility).
 */
public class HandlerChainTest {

    @Test
    public void testSingleHandler() {
        MockLogger logger = new MockLogger();
        LogHandler logHandler = new LogHandler(logger);

        logHandler.handle("Test Report", "test@example.com");

        assertTrue(logger.logged);
    }

    @Test
    public void testChainOfHandlers() {
        MockLogger logger = new MockLogger();
        MockEmailService emailService = new MockEmailService();

        LogHandler logHandler = new LogHandler(logger);
        EmailHandler emailHandler = new EmailHandler(emailService);

        logHandler.setNext(emailHandler);
        logHandler.handle("Test Report", "test@example.com");

        assertTrue(logger.logged);
        assertTrue(emailService.sent);
    }

    @Test
    public void testThreeHandlersChain() {
        MockLogger logger = new MockLogger();
        MockEmailService emailService = new MockEmailService();
        MockArchiveService archiveService = new MockArchiveService();

        LogHandler logHandler = new LogHandler(logger);
        EmailHandler emailHandler = new EmailHandler(emailService);
        ArchiveHandler archiveHandler = new ArchiveHandler(archiveService);

        logHandler.setNext(emailHandler);
        emailHandler.setNext(archiveHandler);

        logHandler.handle("Test Report", "test@example.com");

        assertTrue(logger.logged);
        assertTrue(emailService.sent);
        assertTrue(archiveService.archived);
    }

    // Mock классы
    private static class MockLogger extends Logger {
        boolean logged = false;

        @Override
        public void info(String message) {
            logged = true;
        }
    }

    private static class MockEmailService extends EmailService {
        boolean sent = false;

        @Override
        public void send(String to, String subject, String body) {
            sent = true;
        }
    }

    private static class MockArchiveService {
        boolean archived = false;

        public void archive(String report) {
            archived = true;
        }
    }
}
