public class EmailHandler extends ReportHandler {
    private EmailService emailService;

    public EmailHandler(EmailService emailService) {
        this.emailService = emailService;
    }

    @Override
    protected void process(String report, String recipient) {
        emailService.send(recipient, "Report", report);
    }
}
