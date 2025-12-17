---
layout: default
title: LLM-based Vulnerable Code Augmentation: Generate or Refactor?
---

# LLM-based Vulnerable Code Augmentation: Generate or Refactor?

**arXiv**: [2512.08493v1](https://arxiv.org/abs/2512.08493) | [PDF](https://arxiv.org/pdf/2512.08493.pdf)

**作者**: Dyna Soumhane Ouchebara, Stéphane Dupont

---

## 💡 一句话要点

**提出基于LLM的漏洞代码增强方法，通过生成与重构解决漏洞数据集不平衡问题。**

**关键词**: `漏洞代码增强` `LLM生成` `代码重构` `数据不平衡` `漏洞分类器` `SVEN数据集`

## 📋 核心要点

1. 漏洞代码库存在严重类别不平衡，限制深度学习分类器性能。
2. 比较LLM生成新漏洞样本与重构现有样本的增强策略。
3. 实验表明混合策略能有效提升漏洞分类器在SVEN数据集上的表现。

## 📄 摘要（原文）

> Vulnerability code-bases often suffer from severe imbalance, limiting the effectiveness of Deep Learning-based vulnerability classifiers. Data Augmentation could help solve this by mitigating the scarcity of under-represented CWEs. In this context, we investigate LLM-based augmentation for vulnerable functions, comparing controlled generation of new vulnerable samples with semantics-preserving refactoring of existing ones. Using Qwen2.5-Coder to produce augmented data and CodeBERT as a vulnerability classifier on the SVEN dataset, we find that our approaches are indeed effective in enriching vulnerable code-bases through a simple process and with reasonable quality, and that a hybrid strategy best boosts vulnerability classifiers' performance.

