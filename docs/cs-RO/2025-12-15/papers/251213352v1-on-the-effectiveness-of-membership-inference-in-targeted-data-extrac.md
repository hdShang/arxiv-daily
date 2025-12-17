---
layout: default
title: On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models
---

# On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models

**arXiv**: [2512.13352v1](https://arxiv.org/abs/2512.13352) | [PDF](https://arxiv.org/pdf/2512.13352.pdf)

**作者**: Ali Al Sahili, Ali Chehab, Razane Tajeddine

---

## 💡 一句话要点

**集成多种成员推理攻击技术，评估其在大型语言模型训练数据提取中的有效性**

**关键词**: `大型语言模型` `训练数据提取` `成员推理攻击` `隐私风险` `基准评估`

## 📋 核心要点

1. 核心问题：大型语言模型记忆训练数据，引发隐私风险，包括训练数据提取和成员推理攻击。
2. 方法要点：将多种成员推理攻击技术整合到数据提取流程中，系统评估其性能。
3. 实验或效果：比较集成设置与传统基准下的攻击效果，评估实际提取场景中的实用性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are prone to mem- orizing training data, which poses serious privacy risks. Two of the most prominent concerns are training data extraction and Membership Inference Attacks (MIAs). Prior research has shown that these threats are interconnected: adversaries can extract training data from an LLM by querying the model to generate a large volume of text and subsequently applying MIAs to verify whether a particular data point was included in the training set. In this study, we integrate multiple MIA techniques into the data extraction pipeline to systematically benchmark their effectiveness. We then compare their performance in this integrated setting against results from conventional MIA bench- marks, allowing us to evaluate their practical utility in real-world extraction scenarios.

