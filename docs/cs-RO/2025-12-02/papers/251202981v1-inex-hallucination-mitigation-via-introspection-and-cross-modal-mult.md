---
layout: default
title: InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration
---

# InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration

**arXiv**: [2512.02981v1](https://arxiv.org/abs/2512.02981) | [PDF](https://arxiv.org/pdf/2512.02981.pdf)

**作者**: Zhongyu Yang, Yingfang Yuan, Xuanming Jiang, Baoyi An, Wei Pang

---

## 💡 一句话要点

**提出InEx框架以解决多模态大语言模型中的幻觉问题**

**关键词**: `幻觉缓解` `多模态大语言模型` `多智能体协作` `内省推理` `跨模态验证`

## 📋 核心要点

1. 核心问题：幻觉是多模态大语言模型可靠性的关键挑战，现有方法依赖人工或未充分利用自主缓解能力。
2. 方法要点：基于人类认知范式，通过内省推理和跨模态多智能体协作，实现无训练自主幻觉缓解。
3. 实验或效果：在通用和幻觉基准上优于现有方法，提升4%-27%，展现强鲁棒性。

## 📄 摘要（原文）

> Hallucination remains a critical challenge in large language models (LLMs), hindering the development of reliable multimodal LLMs (MLLMs). Existing solutions often rely on human intervention or underutilize the agent's ability to autonomously mitigate hallucination. To address these limitations, we draw inspiration from how humans make reliable decisions in the real world. They begin with introspective reasoning to reduce uncertainty and form an initial judgment, then rely on external verification from diverse perspectives to reach a final decision. Motivated by this cognitive paradigm, we propose InEx, a training-free, multi-agent framework designed to autonomously mitigate hallucination. InEx introduces internal introspective reasoning, guided by entropy-based uncertainty estimation, to improve the reliability of the decision agent's reasoning process. The agent first generates a response, which is then iteratively verified and refined through external cross-modal multi-agent collaboration with the editing agent and self-reflection agents, further enhancing reliability and mitigating hallucination. Extensive experiments show that InEx consistently outperforms existing methods, achieving 4%-27% gains on general and hallucination benchmarks, and demonstrating strong robustness.

