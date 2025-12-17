---
layout: default
title: Advancing LLM-Based Security Automation with Customized Group Relative Policy Optimization for Zero-Touch Networks
---

# Advancing LLM-Based Security Automation with Customized Group Relative Policy Optimization for Zero-Touch Networks

**arXiv**: [2512.09485v1](https://arxiv.org/abs/2512.09485) | [PDF](https://arxiv.org/pdf/2512.09485.pdf)

**作者**: Xinye Cao, Yihan Lin, Guoshun Nan, Qinchuan Zhou, Yuhang Luo, Yurui Gao, Zeliang Zhang, Haolang Lu, Qimei Cui, Yanzhao Hou, Xiaofeng Tao, Tony Q. S. Quek

---

## 💡 一句话要点

**提出SecLoop和SA-GRPO以解决6G零接触网络中安全自动化的策略生命周期和适应性挑战**

**关键词**: `安全自动化` `零接触网络` `大语言模型` `策略优化` `6G网络` `MITRE ATT&CK`

## 📋 核心要点

1. 核心问题：6G零接触网络面临分布式架构和动态威胁，需自动化安全策略生命周期并适应环境变化。
2. 方法要点：SecLoop集成大语言模型实现安全策略全生命周期自动化；SA-GRPO通过组相对策略优化迭代优化策略。
3. 实验或效果：在真实世界基准测试中验证了方法对多种攻击的有效性，并计划开源平台。

## 📄 摘要（原文）

> Zero-Touch Networks (ZTNs) represent a transformative paradigm toward fully automated and intelligent network management, providing the scalability and adaptability required for the complexity of sixth-generation (6G) networks. However, the distributed architecture, high openness, and deep heterogeneity of 6G networks expand the attack surface and pose unprecedented security challenges. To address this, security automation aims to enable intelligent security management across dynamic and complex environments, serving as a key capability for securing 6G ZTNs. Despite its promise, implementing security automation in 6G ZTNs presents two primary challenges: 1) automating the lifecycle from security strategy generation to validation and update under real-world, parallel, and adversarial conditions, and 2) adapting security strategies to evolving threats and dynamic environments. This motivates us to propose SecLoop and SA-GRPO. SecLoop constitutes the first fully automated framework that integrates large language models (LLMs) across the entire lifecycle of security strategy generation, orchestration, response, and feedback, enabling intelligent and adaptive defenses in dynamic network environments, thus tackling the first challenge. Furthermore, we propose SA-GRPO, a novel security-aware group relative policy optimization algorithm that iteratively refines security strategies by contrasting group feedback collected from parallel SecLoop executions, thereby addressing the second challenge. Extensive real-world experiments on five benchmarks, including 11 MITRE ATT&CK processes and over 20 types of attacks, demonstrate the superiority of the proposed SecLoop and SA-GRPO. We will release our platform to the community, facilitating the advancement of security automation towards next generation communications.

