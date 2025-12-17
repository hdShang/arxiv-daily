---
layout: default
title: Large Causal Models from Large Language Models
---

# Large Causal Models from Large Language Models

**arXiv**: [2512.07796v1](https://arxiv.org/abs/2512.07796) | [PDF](https://arxiv.org/pdf/2512.07796.pdf)

**作者**: Sridhar Mahadevan

---

## 💡 一句话要点

**提出DEMOCRITUS系统，利用大语言模型构建跨领域大型因果模型**

**关键词**: `大型因果模型` `大语言模型` `因果推断` `范畴机器学习` `跨领域建模`

## 📋 核心要点

1. 核心问题：传统因果推断依赖数值实验，难以构建跨领域大型因果模型。
2. 方法要点：使用大语言模型生成因果陈述，通过新范畴机器学习方法整合为因果三元组。
3. 实验或效果：在考古学、生物学、气候变化等多个领域应用，评估系统扩展瓶颈。

## 📄 摘要（原文）

> We introduce a new paradigm for building large causal models (LCMs) that exploits the enormous potential latent in today's large language models (LLMs). We describe our ongoing experiments with an implemented system called DEMOCRITUS (Decentralized Extraction of Manifold Ontologies of Causal Relations Integrating Topos Universal Slices) aimed at building, organizing, and visualizing LCMs that span disparate domains extracted from carefully targeted textual queries to LLMs. DEMOCRITUS is methodologically distinct from traditional narrow domain and hypothesis centered causal inference that builds causal models from experiments that produce numerical data. A high-quality LLM is used to propose topics, generate causal questions, and extract plausible causal statements from a diverse range of domains. The technical challenge is then to take these isolated, fragmented, potentially ambiguous and possibly conflicting causal claims, and weave them into a coherent whole, converting them into relational causal triples and embedding them into a LCM. Addressing this technical challenge required inventing new categorical machine learning methods, which we can only briefly summarize in this paper, as it is focused more on the systems side of building DEMOCRITUS. We describe the implementation pipeline for DEMOCRITUS comprising of six modules, examine its computational cost profile to determine where the current bottlenecks in scaling the system to larger models. We describe the results of using DEMOCRITUS over a wide range of domains, spanning archaeology, biology, climate change, economics, medicine and technology. We discuss the limitations of the current DEMOCRITUS system, and outline directions for extending its capabilities.

