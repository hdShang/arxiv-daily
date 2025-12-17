---
layout: default
title: LLMs Can Assist with Proposal Selection at Large User Facilities
---

# LLMs Can Assist with Proposal Selection at Large User Facilities

**arXiv**: [2512.10895v1](https://arxiv.org/abs/2512.10895) | [PDF](https://arxiv.org/pdf/2512.10895.pdf)

**作者**: Lijie Ding, Janell Thomson, Jon Taylor, Changwoo Do

---

## 💡 一句话要点

**提出基于大语言模型的提案选择方法，以提升大型用户设施中提案评审的效率和一致性。**

**关键词**: `大语言模型` `提案选择` `成对偏好` `评审自动化` `成本效益` `提案相似性分析`

## 📋 核心要点

1. 核心问题：传统人工评审存在提案间相关性弱、评审者偏见和不一致性问题。
2. 方法要点：采用基于成对偏好的LLM方法，替代人工进行提案排序，实现更严谨的内部一致性。
3. 实验或效果：LLM排序与人工排序强相关（Spearman ρ约0.2-0.8），成本降低两个数量级以上，且能进行提案相似性等高级分析。

## 📄 摘要（原文）

> We explore how large language models (LLMs) can enhance the proposal selection process at large user facilities, offering a scalable, consistent, and cost-effective alternative to traditional human review. Proposal selection depends on assessing the relative strength among submitted proposals; however, traditional human scoring often suffers from weak inter-proposal correlations and is subject to reviewer bias and inconsistency. A pairwise preference-based approach is logically superior, providing a more rigorous and internally consistent basis for ranking, but its quadratic workload makes it impractical for human reviewers. We address this limitation using LLMs. Leveraging the uniquely well-curated proposals and publication records from three beamlines at the Spallation Neutron Source (SNS), Oak Ridge National Laboratory (ORNL), we show that the LLM rankings correlate strongly with the human rankings (Spearman $ρ\simeq 0.2-0.8$, improving to $\geq 0.5$ after 10\% outlier removal). Moreover, LLM performance is no worse than that of human reviewers in identifying proposals with high publication potential, while costing over two orders of magnitude less. Beyond ranking, LLMs enable advanced analyses that are challenging for humans, such as quantitative assessment of proposal similarity via embedding models, which provides information crucial for review committees.

