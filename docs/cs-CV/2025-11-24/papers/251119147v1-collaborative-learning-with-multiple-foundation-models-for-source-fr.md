---
layout: default
title: Collaborative Learning with Multiple Foundation Models for Source-Free Domain Adaptation
---

# Collaborative Learning with Multiple Foundation Models for Source-Free Domain Adaptation

**arXiv**: [2511.19147v1](https://arxiv.org/abs/2511.19147) | [PDF](https://arxiv.org/pdf/2511.19147.pdf)

**作者**: Huisoo Lee, Jisu Han, Hyunsouk Cho, Wonjun Hwang

---

## 💡 一句话要点

**提出CoMA框架，利用互补基础模型解决源自由域适应中的语义覆盖不足问题**

**关键词**: `源自由域适应` `基础模型协作` `双向适应机制` `分解互信息` `语义知识传递` `目标域适应`

## 📋 核心要点

1. 源自由域适应中，单一基础模型易导致语义覆盖受限，无法捕捉多样上下文线索
2. 采用双向适应机制，结合CLIP和BLIP等模型，传递互补知识并保持语义独特性
3. 在多个基准测试中，CoMA在闭集、部分集和开放集设置下均优于现有方法

## 📄 摘要（原文）

> Source-Free Domain Adaptation (SFDA) aims to adapt a pre-trained source model to an unlabeled target domain without access to source data. Recent advances in Foundation Models (FMs) have introduced new opportunities for leveraging external semantic knowledge to guide SFDA. However, relying on a single FM is often insufficient, as it tends to bias adaptation toward a restricted semantic coverage, failing to capture diverse contextual cues under domain shift. To overcome this limitation, we propose a Collaborative Multi-foundation Adaptation (CoMA) framework that jointly leverages two different FMs (e.g., CLIP and BLIP) with complementary properties to capture both global semantics and local contextual cues. Specifically, we employ a bidirectional adaptation mechanism that (1) aligns different FMs with the target model for task adaptation while maintaining their semantic distinctiveness, and (2) transfers complementary knowledge from the FMs to the target model. To ensure stable adaptation under mini-batch training, we introduce Decomposed Mutual Information (DMI) that selectively enhances true dependencies while suppressing false dependencies arising from incomplete class coverage. Extensive experiments demonstrate that our method consistently outperforms existing state-of-the-art SFDA methods across four benchmarks, including Office-31, Office-Home, DomainNet-126, and VisDA, under the closed-set setting, while also achieving best results on partial-set and open-set variants.

