from core._mysql import base, engine

print('+++++++++++++++++++++++++++')
base.metadata.create_all(engine)