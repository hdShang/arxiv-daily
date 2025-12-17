---
layout: default
title: Towards Privacy-Preserving Code Generation: Differentially Private Code Language Models
---

# Towards Privacy-Preserving Code Generation: Differentially Private Code Language Models

**arXiv**: [2512.11482v1](https://arxiv.org/abs/2512.11482) | [PDF](https://arxiv.org/pdf/2512.11482.pdf)

**作者**: Melih Catal, Pooja Rani, Harald C. Gall

---

## 💡 一句话要点

**应用差分隐私于代码语言模型以缓解记忆风险并保持生成能力**

**关键词**: `差分隐私` `代码语言模型` `隐私保护` `代码生成` `模型训练` `记忆缓解`

## 📋 核心要点

1. 代码语言模型在训练中可能记忆并泄露敏感代码片段，引发隐私和知识产权风险
2. 通过差分隐私在训练过程中添加校准噪声，有效减少记忆行为而不显著损害模型性能
3. 实验显示差分隐私大幅降低记忆率，轻微增加困惑度，且对训练效率和能耗影响小

## 📄 摘要（原文）

> Large language models specialized for code (CodeLLMs) have demonstrated remarkable capabilities in generating code snippets, documentation, and test cases. However, despite their promising capabilities, CodeLLMs can inadvertently memorize and reproduce snippets from their training data, which poses risks of privacy breaches and intellectual property violations. These risks restrict the deployment of CodeLLMs in sensitive domains and limit their training datasets to publicly available sources. To mitigate the memorization risk without compromising their task performance, we apply Differential Privacy (DP) to CodeLLMs. To the best of our knowledge, this is the first comprehensive study that systematically evaluates the effectiveness of DP in CodeLLMs. DP adds calibrated noise to the training process to protect individual data points while still allowing the model to learn useful patterns. To this end, we first identify and understand the driving reasons of the memorization behaviour of the CodeLLMs during their fine-tuning. Then, to address this issue, we empirically evaluate the effect of DP on mitigating memorization while preserving code generation capabilities. Our findings show that DP substantially reduces memorization in CodeLLMs across all the tested snippet types. The snippet types most prone to memorization are also the most effectively mitigated by DP. Furthermore, we observe that DP slightly increases perplexity but preserves, and can even enhance, the code generation capabilities of CodeLLMs, which makes it feasible to apply DP in practice without significantly compromising model utility. Finally, we analyze the impact of DP on training efficiency and energy consumption, finding that DP does not significantly affect training time or energy usage, making it a practical choice for privacy-preserving CodeLLMs training.

