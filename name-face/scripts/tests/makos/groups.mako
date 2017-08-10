<row>
    <gid><![CDATA[1]]></gid>
    <sid><![CDATA[900000]]></sid>
    <group_name><![CDATA[Intro]]></group_name>
    <group_order><![CDATA[0]]></group_order>
    <description><![CDATA[<p>Welkom</p>
]]></description>
    <language><![CDATA[en]]></language>
    <randomization_group/>
    <grelevance/>
</row>
% for i in range(starting_group_id + 1, starting_group_id + len(questions) + 1):
<row>
    <gid><![CDATA[${i}]]></gid>
    <sid><![CDATA[900000]]></sid>
    <group_name><![CDATA[Q${i}]]></group_name>
    <group_order><![CDATA[${i}]]></group_order>
    <description/>
    <language><![CDATA[en]]></language>
    <randomization_group/>
    <grelevance/>
</row>
% endfor