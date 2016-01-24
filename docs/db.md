# Current database Structure

device:
  int: id
  str: model
  str: image (base64 data uri)

build:
  int: id
  int: device_id
  str: path
  int: size
  str: md5sum
  str: sha1sum
  str: sha512
  int: type_id
  int: build_number
  str: fingerprint
  str: description
  date: created
  date: updated
  int: recovery_id

recovery:
  int: id
  str: path
  date: created
  date: updated
  str: sha1sum
  str: sha512

type:
  int: id
  str: name

stats:
  int: id
  str: device_hash
  date: created
  date: last_checkin
  int: model_id

mirror:
  int: id
  str: basepath
  int: weight
  str: region
  bool: available
