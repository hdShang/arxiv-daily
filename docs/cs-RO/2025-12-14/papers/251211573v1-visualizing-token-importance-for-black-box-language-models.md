---
layout: default
title: Visualizing token importance for black-box language models
---

# Visualizing token importance for black-box language models

**arXiv**: [2512.11573v1](https://arxiv.org/abs/2512.11573) | [PDF](https://arxiv.org/pdf/2512.11573.pdf)

**作者**: Paulius Rauba, Qiyao Wei, Mihaela van der Schaar

---

## 💡 一句话要点

**提出分布敏感性分析以评估黑盒语言模型输入令牌重要性**

**关键词**: `黑盒语言模型` `令牌重要性` `敏感性分析` `模型审计` `可解释性`

## 📋 核心要点

1. 核心问题：审计黑盒LLM输出对输入令牌的依赖，确保高风险领域可靠性
2. 方法要点：开发轻量级模型无关的DBSA，无需分布假设，可视化令牌敏感性
3. 实验或效果：通过示例展示DBSA能发现现有方法忽略的敏感性，支持快速探索

## 📄 摘要（原文）

> We consider the problem of auditing black-box large language models (LLMs) to ensure they behave reliably when deployed in production settings, particularly in high-stakes domains such as legal, medical, and regulatory compliance. Existing approaches for LLM auditing often focus on isolated aspects of model behavior, such as detecting specific biases or evaluating fairness. We are interested in a more general question -- can we understand how the outputs of black-box LLMs depend on each input token? There is a critical need to have such tools in real-world applications that rely on inaccessible API endpoints to language models. However, this is a highly non-trivial problem, as LLMs are stochastic functions (i.e. two outputs will be different by chance), while computing prompt-level gradients to approximate input sensitivity is infeasible. To address this, we propose Distribution-Based Sensitivity Analysis (DBSA), a lightweight model-agnostic procedure to evaluate the sensitivity of the output of a language model for each input token, without making any distributional assumptions about the LLM. DBSA is developed as a practical tool for practitioners, enabling quick, plug-and-play visual exploration of LLMs reliance on specific input tokens. Through illustrative examples, we demonstrate how DBSA can enable users to inspect LLM inputs and find sensitivities that may be overlooked by existing LLM interpretability methods.

