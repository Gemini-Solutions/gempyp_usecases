from gempyp.libs.enums.status import status
class BeforeAfter:
    def before(self,obj):
        obj.reporter.addRow("testing before method", "working fine",status.INFO)
        return obj