---
layout: default
title: Massive Editing for Large Language Models Based on Dynamic Weight Generation
---

# Massive Editing for Large Language Models Based on Dynamic Weight Generation

**arXiv**: [2512.14395v1](https://arxiv.org/abs/2512.14395) | [PDF](https://arxiv.org/pdf/2512.14395.pdf)

**作者**: Wentao Wan, Qiqing Lao, Zhiwei Xie, Hefeng Wu, Runnan Lin, Liang Lin, Keze Wang

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: 27 pages, 8 figures

---

## 💡 一句话要点

**提出基于动态权重生成的大规模编辑方法MeG，以解决大语言模型知识编辑中的大规模修改挑战。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `知识编辑` `大语言模型` `动态权重生成` `扩散模型` `大规模编辑` `神经元附加` `模型优化` `条件生成`

## 📋 核心要点

1. 现有知识编辑方法难以在大规模修改时同时保证可靠性、通用性和局部性，导致编辑效果受限。
2. MeG通过附加动态权重神经元，利用扩散模型根据输入查询生成权重，实现单神经元支持大规模编辑。
3. 实验显示MeG在可靠性、通用性和局部性指标上显著优于现有方法，局部性提升尤为突出。

## 📝 摘要（中文）

知识编辑（KE）是研究如何以低成本（相比预训练）修改大语言模型（LLMs）中某些知识的领域。目前，在对LLMs进行大规模编辑的同时，确保编辑的可靠性、通用性和局部性指标仍是一个挑战。本文提出了一种基于动态权重生成的大规模编辑方法（MeG）。我们的MeG涉及在LLMs的特定层附加一个动态权重神经元，并使用扩散模型根据知识所需的输入查询条件生成该神经元的权重。这使得通过添加单个动态权重神经元即可实现大规模知识编辑的目标。实验表明，与现有知识编辑方法相比，我们的MeG在可靠性、通用性和局部性指标方面能显著提升大规模KE的性能，特别是局部性指标的绝对值指数有较高的百分点提升，证明了我们提出方法的优势。

## 🔬 方法详解

MeG的整体框架是在大语言模型的特定层中附加一个动态权重神经元，该神经元的权重不固定，而是由扩散模型根据输入查询条件生成。关键技术创新在于将知识编辑问题转化为权重生成问题，通过扩散模型学习查询与编辑权重之间的映射关系，从而实现灵活的大规模编辑。与现有方法主要区别在于，传统方法通常依赖静态参数修改或外部存储，而MeG通过动态权重生成机制，仅需添加单个神经元即可适应多种编辑需求，提高了编辑的效率和可扩展性。

## 📊 实验亮点

MeG在可靠性、通用性和局部性指标上均显著优于现有知识编辑方法，特别是局部性指标的绝对值指数有较高百分点提升，验证了其在大规模编辑场景下的优越性能。

## 🎯 应用场景

该研究可应用于大语言模型的快速知识更新、错误修正和个性化定制，例如在对话系统、内容生成和知识库维护中，实现低成本、高效率的模型调整，提升AI系统的适应性和准确性。

## 📄 摘要（原文）

> Knowledge Editing (KE) is a field that studies how to modify some knowledge in Large Language Models (LLMs) at a low cost (compared to pre-training). Currently, performing large-scale edits on LLMs while ensuring the Reliability, Generality, and Locality metrics of the edits remain a challenge. This paper proposes a Massive editing approach for LLMs based on dynamic weight Generation (MeG). Our MeG involves attaching a dynamic weight neuron to specific layers of the LLMs and using a diffusion model to conditionally generate the weights of this neuron based on the input query required for the knowledge. This allows the use of adding a single dynamic weight neuron to achieve the goal of large-scale knowledge editing. Experiments show that our MeG can significantly improve the performance of large-scale KE in terms of Reliability, Generality, and Locality metrics compared to existing knowledge editing methods, particularly with a high percentage point increase in the absolute value index for the Locality metric, demonstrating the advantages of our proposed method.

