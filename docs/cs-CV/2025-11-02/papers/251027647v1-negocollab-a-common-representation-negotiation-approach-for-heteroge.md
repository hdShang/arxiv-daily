---
layout: default
title: NegoCollab: A Common Representation Negotiation Approach for Heterogeneous Collaborative Perception
---

# NegoCollab: A Common Representation Negotiation Approach for Heterogeneous Collaborative Perception

**arXiv**: [2510.27647v1](https://arxiv.org/abs/2510.27647) | [PDF](https://arxiv.org/pdf/2510.27647.pdf)

**作者**: Congzhang Shao, Quan Yuan, Guiyang Luo, Yue Hu, Danni Wang, Yilin Liu, Rui Pan, Bo Chen, Jinglin Li

---

## 💡 一句话要点

**提出NegoCollab以解决异构协作感知中的特征域差距问题**

**关键词**: `协作感知` `异构代理` `特征对齐` `共同表示` `多模态信息` `训练损失`

## 📋 核心要点

1. 核心问题：异构代理使用不同感知模型导致特征共享时出现域差距，降低协作性能
2. 方法要点：引入协商器从各代理局部表示中推导共同表示，减少域差距
3. 实验或效果：通过结构、语用和对齐损失监督训练，提升协作感知性能

## 📄 摘要（原文）

> Collaborative perception improves task performance by expanding the
> perception range through information sharing among agents. . Immutable
> heterogeneity poses a significant challenge in collaborative perception, as
> participating agents may employ different and fixed perception models. This
> leads to domain gaps in the intermediate features shared among agents,
> consequently degrading collaborative performance. Aligning the features of all
> agents to a common representation can eliminate domain gaps with low training
> cost. However, in existing methods, the common representation is designated as
> the representation of a specific agent, making it difficult for agents with
> significant domain discrepancies from this specific agent to achieve proper
> alignment. This paper proposes NegoCollab, a heterogeneous collaboration method
> based on the negotiated common representation. It introduces a negotiator
> during training to derive the common representation from the local
> representations of each modality's agent, effectively reducing the inherent
> domain gap with the various local representations. In NegoCollab, the mutual
> transformation of features between the local representation space and the
> common representation space is achieved by a pair of sender and receiver. To
> better align local representations to the common representation containing
> multimodal information, we introduce structural alignment loss and pragmatic
> alignment loss in addition to the distribution alignment loss to supervise the
> training. This enables the knowledge in the common representation to be fully
> distilled into the sender.

