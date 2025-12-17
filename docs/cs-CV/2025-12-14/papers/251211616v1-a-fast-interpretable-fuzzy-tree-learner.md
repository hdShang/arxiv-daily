---
layout: default
title: A Fast Interpretable Fuzzy Tree Learner
---

# A Fast Interpretable Fuzzy Tree Learner

**arXiv**: [2512.11616v1](https://arxiv.org/abs/2512.11616) | [PDF](https://arxiv.org/pdf/2512.11616.pdf)

**作者**: Javier Fumanal-Idocin, Raquel Fernandez-Peralta, Javier Andreu-Perez

---

## 💡 一句话要点

**提出模糊贪婪树算法，以高效生成可解释模糊规则，用于表格分类任务。**

**关键词**: `模糊规则系统` `可解释机器学习` `贪婪树算法` `表格分类` `计算效率`

## 📋 核心要点

1. 核心问题：现有模糊规则挖掘算法难以同时保证可解释性（合理语言划分和小规则库）与计算效率。
2. 方法要点：将经典树分裂算法从清晰规则扩展到模糊树，结合贪婪算法效率和模糊逻辑可解释性优势。
3. 实验或效果：在表格分类基准上，相比进化方法显著降低计算成本，保持竞争性预测性能，生成更可解释规则库。

## 📄 摘要（原文）

> Fuzzy rule-based systems have been mostly used in interpretable decision-making because of their interpretable linguistic rules. However, interpretability requires both sensible linguistic partitions and small rule-base sizes, which are not guaranteed by many existing fuzzy rule-mining algorithms. Evolutionary approaches can produce high-quality models but suffer from prohibitive computational costs, while neural-based methods like ANFIS have problems retaining linguistic interpretations. In this work, we propose an adaptation of classical tree-based splitting algorithms from crisp rules to fuzzy trees, combining the computational efficiency of greedy algoritms with the interpretability advantages of fuzzy logic. This approach achieves interpretable linguistic partitions and substantially improves running time compared to evolutionary-based approaches while maintaining competitive predictive performance. Our experiments on tabular classification benchmarks proof that our method achieves comparable accuracy to state-of-the-art fuzzy classifiers with significantly lower computational cost and produces more interpretable rule bases with constrained complexity. Code is available in: https://github.com/Fuminides/fuzzy_greedy_tree_public

