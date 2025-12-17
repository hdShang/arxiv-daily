---
layout: default
title: From User Interface to Agent Interface: Efficiency Optimization of UI Representations for LLM Agents
---

# From User Interface to Agent Interface: Efficiency Optimization of UI Representations for LLM Agents

**arXiv**: [2512.13438v1](https://arxiv.org/abs/2512.13438) | [PDF](https://arxiv.org/pdf/2512.13438.pdf)

**作者**: Dezhi Ran, Zhi Gong, Yuzhe Guo, Mengzhou Wu, Yuan Cao, Haochuan Lu, Hengyu Zhang, Xia Zeng, Gang Cao, Liangchao Yao, Yuetang Deng, Wei Yang, Tao Xie

---

## 💡 一句话要点

**提出UIFormer框架以优化UI表示，提升LLM代理在自动化UI导航中的效率**

**关键词**: `UI表示优化` `LLM代理` `程序合成` `自动化UI导航` `效率提升`

## 📋 核心要点

1. 核心问题：UI表示效率低下成为LLM代理性能瓶颈，缺乏布尔预言机阻碍语义正确性验证
2. 方法要点：基于DSL限制程序空间，结合LLM迭代优化，实现效率与完整性的协同优化
3. 实验或效果：在Android和Web基准测试中实现48.7%至55.8%的令牌减少，保持或提升代理性能

## 📄 摘要（原文）

> While Large Language Model (LLM) agents show great potential for automated UI navigation such as automated UI testing and AI assistants, their efficiency has been largely overlooked. Our motivating study reveals that inefficient UI representation creates a critical performance bottleneck. However, UI representation optimization, formulated as the task of automatically generating programs that transform UI representations, faces two unique challenges. First, the lack of Boolean oracles, which traditional program synthesis uses to decisively validate semantic correctness, poses a fundamental challenge to co-optimization of token efficiency and completeness. Second, the need to process large, complex UI trees as input while generating long, compositional transformation programs, making the search space vast and error-prone. Toward addressing the preceding limitations, we present UIFormer, the first automated optimization framework that synthesizes UI transformation programs by conducting constraint-based optimization with structured decomposition of the complex synthesis task. First, UIFormer restricts the program space using a domain-specific language (DSL) that captures UI-specific operations. Second, UIFormer conducts LLM-based iterative refinement with correctness and efficiency rewards, providing guidance for achieving the efficiency-completeness co-optimization. UIFormer operates as a lightweight plugin that applies transformation programs for seamless integration with existing LLM agents, requiring minimal modifications to their core logic. Evaluations across three UI navigation benchmarks spanning Android and Web platforms with five LLMs demonstrate that UIFormer achieves 48.7% to 55.8% token reduction with minimal runtime overhead while maintaining or improving agent performance. Real-world industry deployment at WeChat further validates the practical impact of UIFormer.

