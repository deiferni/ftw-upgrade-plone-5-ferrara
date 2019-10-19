#doitlive speed: 2

bin/instance start
bin/upgrade list -S -u
bin/upgrade install -S -u 20191008190813@ftwupgrade.demo:default

bin/upgrade create "Demo upgrade step." --path=src/ftwupgrade/demo/upgrades/
bin/instance restart
bin/upgrade list -S -u
bin/upgrade install -S -p
