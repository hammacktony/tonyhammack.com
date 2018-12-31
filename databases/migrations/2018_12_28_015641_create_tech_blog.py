''' Migration file for Posts table  '''
from orator.migrations import Migration


class CreateTechTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.connection('connection_2').create('tech') as table:
            table.increments('id')
            table.string('slug')
            table.string('title')

            table.string('image').nullable()
            table.string('category').nullable()

            table.integer('author_id').unsigned()
            table.foreign('author_id').references('id').on('users')

            table.string('body', 10485760)
            table.timestamps()

            table.integer('is_live').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.connection('connection2').drop('tech')