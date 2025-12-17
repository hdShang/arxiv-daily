---
layout: default
title: R3A: Reliable RTL Repair Framework with Multi-Agent Fault Localization and Stochastic Tree-of-Thoughts Patch Generation
---

# R3A: Reliable RTL Repair Framework with Multi-Agent Fault Localization and Stochastic Tree-of-Thoughts Patch Generation

**arXiv**: [2511.20090v1](https://arxiv.org/abs/2511.20090) | [PDF](https://arxiv.org/pdf/2511.20090.pdf)

**作者**: Zizhang Luo, Fan Cui, Kexing Zhou, Runlin Guo, Mile Xia, Hongyuan Hou, Yun Lian

---

## 💡 一句话要点

**提出R3A框架以解决RTL代码修复的可靠性问题**

**关键词**: `RTL修复` `多智能体系统` `思维树算法` `故障定位` `程序合成` `大语言模型`

## 📋 核心要点

1. 传统RTL修复方法依赖固定模板，处理能力有限
2. R3A结合多智能体故障定位和随机思维树方法提升修复可靠性
3. 实验显示R3A修复90.6%的bug，覆盖率和通过率显著提升

## 📄 摘要（原文）

> Repairing RTL bugs is crucial for hardware design and verification. Traditional automatic program repair (APR) methods define dedicated search spaces to locate and fix bugs with program synthesis. However, they heavily rely on fixed templates and can only deal with limited bugs. As an alternative, Large Language Models with the ability to understand code semantics can be explored for RTL repair. However, they suffer from unreliable outcomes due to inherent randomness and long input contexts of RTL code and waveform. To address these challenges, we propose R3A, an LLM-based automatic RTL program repair framework upon the basic model to improve reliability. R3A proposes the stochastic Tree-Of-Thoughts method to control a patch generation agent to explore a validated solution for the bug. The algorithm samples search states according to a heuristic function to balance between exploration and exploitation for a reliable outcome. Besides, R3A proposes a multi-agent fault localization method to find fault candidates as the starting points for the patch generation agent, further increasing the reliability. Experiments show R3A can fix 90.6% of bugs in the RTL-repair dataset within a given time limit, which covers 45% more bugs than traditional methods and other LLM-based approaches, while achieving an 86.7% pass@5 rate on average, showing a high reliability.

