---
layout: default
title: CoSineVerifier: Tool-Augmented Answer Verification for Computation-Oriented Scientific Questions
---

# CoSineVerifier: Tool-Augmented Answer Verification for Computation-Oriented Scientific Questions

**arXiv**: [2512.01224v1](https://arxiv.org/abs/2512.01224) | [PDF](https://arxiv.org/pdf/2512.01224.pdf)

**作者**: Ruixiang Feng, Zhenwei An, Yuntao Wen, Ran Le, Yiming Jia, Chen Yang, Zongchao Chen, Lisi Chen, Shen Gao, Shuo Shang, Yang Song, Tao Zhang

---

## 💡 一句话要点

**提出CoSineVerifier工具增强验证器，以解决计算导向科学问题中的答案验证挑战。**

**关键词**: `答案验证` `工具增强` `计算导向科学` `强化学习` `符号简化` `STEM评估`

## 📋 核心要点

1. 核心问题：计算导向科学领域如代数等价检查和物理常数替换的答案验证存在困难。
2. 方法要点：采用工具增强方法，结合外部执行器进行精确计算和符号简化。
3. 实验或效果：在STEM、通用QA和长推理任务上表现优异，在VerifyBench-Hard和SCI-Bench达到SOTA。

## 📄 摘要（原文）

> Answer verification methods are widely employed in language model training pipelines spanning data curation, evaluation, and reinforcement learning with verifiable rewards (RLVR). While prior work focus on developing unified verifiers applicable across multiple reasoning scenarios, significant challenges remain in computation-oriented scientific domains, such as algebraic equivalence checking and physical constant substitution. In this paper, we introduce \model, a tool-augmented verifier that leverages external executors to perform precise computations and symbolic simplifications. \model enables robust verification that goes beyond simple semantic matching. We propose a novel two-stage pipeline, which begin with cold-start fine-tuning and followed by multi-turn reinforcement learning with tool integration. Extensive experiments conducted on STEM subjects, general QA, and long-form reasoning tasks demonstrates strong generalization of \model. The results shows that the \model achieves state-of-the-art performance on VerifyBench-Hard and SCI-Bench. And we also employ our \model in RLVR as a reward model, the results show that it consistently outperforms both rubric-based and model-based verifiers on AIME'24 and AIME'25, demonstrating strong potential to enhance reasoning capabilities of LLM. Our model is released at \hyperlink{https://huggingface.co/Nanbeige/CoSineVerifier-Tool-4B}{https://huggingface.co/Nanbeige/CoSineVerifier-Tool-4B}.

