---
layout: default
title: Argus: A Multi-Agent Sensitive Information Leakage Detection Framework Based on Hierarchical Reference Relationships
---

# Argus: A Multi-Agent Sensitive Information Leakage Detection Framework Based on Hierarchical Reference Relationships

**arXiv**: [2512.08326v1](https://arxiv.org/abs/2512.08326) | [PDF](https://arxiv.org/pdf/2512.08326.pdf)

**作者**: Bin Wang, Hui Li, Liyang Zhang, Qijia Zhuang, Ao Yang, Dong Zhang, Xijun Luo, Bing Lin

---

## 💡 一句话要点

**提出Argus多智能体框架，基于分层参考关系检测代码库敏感信息泄露，降低误报率。**

**关键词**: `敏感信息泄露检测` `多智能体协作` `分层参考关系` `代码库安全` `大语言模型应用` `误报率降低`

## 📋 核心要点

1. 核心问题：传统敏感信息检测方法误报率高，增加开发者手动筛查负担。
2. 方法要点：采用三层检测机制，结合内容、文件上下文和项目参考关系，多智能体协作。
3. 实验或效果：在真实仓库测试中，准确率达94.86%，成本仅2.2美元，代码开源。

## 📄 摘要（原文）

> Sensitive information leakage in code repositories has emerged as a critical security challenge. Traditional detection methods that rely on regular expressions, fingerprint features, and high-entropy calculations often suffer from high false-positive rates. This not only reduces detection efficiency but also significantly increases the manual screening burden on developers. Recent advances in large language models (LLMs) and multi-agent collaborative architectures have demonstrated remarkable potential for tackling complex tasks, offering a novel technological perspective for sensitive information detection. In response to these challenges, we propose Argus, a multi-agent collaborative framework for detecting sensitive information. Argus employs a three-tier detection mechanism that integrates key content, file context, and project reference relationships to effectively reduce false positives and enhance overall detection accuracy. To comprehensively evaluate Argus in real-world repository environments, we developed two new benchmarks, one to assess genuine leak detection capabilities and another to evaluate false-positive filtering performance. Experimental results show that Argus achieves up to 94.86% accuracy in leak detection, with a precision of 96.36%, recall of 94.64%, and an F1 score of 0.955. Moreover, the analysis of 97 real repositories incurred a total cost of only 2.2$. All code implementations and related datasets are publicly available at https://github.com/TheBinKing/Argus-Guard for further research and application.

