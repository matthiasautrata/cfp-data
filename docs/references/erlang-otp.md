## Erlang/OTP

- **Home**: https://www.erlang.org/
- **Key concepts**: Isolated processes that communicate only by messages; supervision trees that restart failed processes; code upgrades while the system runs. Built at Ericsson for telecom switching; also behind messaging back ends such as WhatsApp's
- **Relevance**: Loose architectural inspiration for pluggable producers and agents that connect by messages, fail in isolation, and can be replaced without stopping the system
- **Used by**: [Idea: extensible fact protocol](../ideas/extensible-fact-protocol.md), [Idea: multi-agent coordination](../ideas/multi-agent-coordination.md)
