from django.db import models
from user_streams.backends.utils import get_user_model_fk_ref


class SingleUserStreamItem(models.Model):

    user = models.ForeignKey(get_user_model_fk_ref(), related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']
        db_table = 'user_streams_single_table_backend_streamitem'
