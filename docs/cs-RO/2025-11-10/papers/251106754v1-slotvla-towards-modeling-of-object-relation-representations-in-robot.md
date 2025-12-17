---
layout: default
title: SlotVLA: Towards Modeling of Object-Relation Representations in Robotic Manipulation
---

# SlotVLA: Towards Modeling of Object-Relation Representations in Robotic Manipulation

**arXiv**: [2511.06754v1](https://arxiv.org/abs/2511.06754) | [PDF](https://arxiv.org/pdf/2511.06754.pdf)

**作者**: Taisei Hanyu, Nhat Chung, Huy Le, Toan Nguyen, Yuki Ikebe, Anthony Gunderman, Duy Nguyen Ho Minh, Khoa Vo, Tung Kieu, Kashu Yamazaki, Chase Rainwater, Anh Nguyen, Ngan Le

---

## 💡 一句话要点

**提出SlotVLA框架和LIBERO+数据集，以提升机器人操作中的对象关系建模效率与可解释性。**

**关键词**: `机器人操作` `对象关系建模` `槽注意力` `多任务学习` `可解释AI` `视觉语言模型`

## 📋 核心要点

1. 核心问题：现有机器人多任务模型依赖密集嵌入，导致对象与背景信息纠缠，影响效率和可解释性。
2. 方法要点：引入SlotVLA框架，使用槽注意力捕获对象及其关系，结合LLM模块生成可执行动作。
3. 实验或效果：在LIBERO+数据集上验证，对象中心表示显著减少视觉令牌数量，保持竞争性泛化能力。

## 📄 摘要（原文）

> Inspired by how humans reason over discrete objects and their relationships,
> we explore whether compact object-centric and object-relation representations
> can form a foundation for multitask robotic manipulation. Most existing robotic
> multitask models rely on dense embeddings that entangle both object and
> background cues, raising concerns about both efficiency and interpretability.
> In contrast, we study object-relation-centric representations as a pathway to
> more structured, efficient, and explainable visuomotor control. Our
> contributions are two-fold. First, we introduce LIBERO+, a fine-grained
> benchmark dataset designed to enable and evaluate object-relation reasoning in
> robotic manipulation. Unlike prior datasets, LIBERO+ provides object-centric
> annotations that enrich demonstrations with box- and mask-level labels as well
> as instance-level temporal tracking, supporting compact and interpretable
> visuomotor representations. Second, we propose SlotVLA, a slot-attention-based
> framework that captures both objects and their relations for action decoding.
> It uses a slot-based visual tokenizer to maintain consistent temporal object
> representations, a relation-centric decoder to produce task-relevant
> embeddings, and an LLM-driven module that translates these embeddings into
> executable actions. Experiments on LIBERO+ demonstrate that object-centric slot
> and object-relation slot representations drastically reduce the number of
> required visual tokens, while providing competitive generalization. Together,
> LIBERO+ and SlotVLA provide a compact, interpretable, and effective foundation
> for advancing object-relation-centric robotic manipulation.

