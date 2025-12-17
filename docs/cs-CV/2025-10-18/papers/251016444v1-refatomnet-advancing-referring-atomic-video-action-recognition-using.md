---
layout: default
title: RefAtomNet++: Advancing Referring Atomic Video Action Recognition using Semantic Retrieval based Multi-Trajectory Mamba
---

# RefAtomNet++: Advancing Referring Atomic Video Action Recognition using Semantic Retrieval based Multi-Trajectory Mamba

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16444" target="_blank" class="toolbar-btn">arXiv: 2510.16444v1</a>
    <a href="https://arxiv.org/pdf/2510.16444.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16444v1" 
            onclick="toggleFavorite(this, '2510.16444v1', 'RefAtomNet++: Advancing Referring Atomic Video Action Recognition using Semantic Retrieval based Multi-Trajectory Mamba')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kunyu Peng, Di Wen, Jia Fu, Jiamin Wu, Kailun Yang, Junwei Zheng, Ruiping Liu, Yufan Chen, Yuqian Fu, Danda Pani Paudel, Luc Van Gool, Rainer Stiefelhagen

**分类**: cs.CV, cs.MM, cs.RO, eess.IV

**发布日期**: 2025-10-18

**备注**: Extended version of ECCV 2024 paper arXiv:2407.01872. The dataset and code are released at https://github.com/KPeng9510/refAVA2

**🔗 代码/项目**: [GITHUB](https://github.com/KPeng9510/refAVA2)

---

## 💡 一句话要点

**RefAtomNet++：利用语义检索的多轨迹Mamba推进指代表达式原子视频动作识别**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `指代表达式理解` `原子动作识别` `视频理解` `跨模态学习` `Mamba模型` `语义对齐` `多层次建模`

## 📋 核心要点

1. 现有RAVAR方法在跨模态信息对齐和检索方面存在局限性，难以精确定位目标人物和预测细粒度动作。
2. RefAtomNet++通过多层次语义对齐的交叉注意机制和多轨迹Mamba建模，增强跨模态token的聚合能力。
3. 实验结果表明，RefAtomNet++在RefAVA++数据集上取得了state-of-the-art的性能，显著提升了RAVAR的准确性。

## 📝 摘要（中文）

指代表达式原子视频动作识别(RAVAR)旨在识别在自然语言描述条件下，特定人物的细粒度原子级别动作。与传统的动作识别和检测任务不同，RAVAR强调精确的语言引导动作理解，这对于复杂多人场景中的交互式人类动作分析至关重要。本文扩展了之前提出的RefAVA数据集到RefAVA++，总共包含超过290万帧和超过75.1k个标注人物。我们使用来自多个相关领域的基线模型（包括原子动作定位、视频问答和文本视频检索）以及我们之前的模型RefAtomNet来评估该数据集。虽然RefAtomNet通过结合代理注意力来突出显著特征，从而超越了其他基线，但其对齐和检索跨模态信息的能力仍然有限，导致在定位目标人物和预测细粒度动作方面的性能欠佳。为了克服上述限制，我们引入了RefAtomNet++，这是一个新颖的框架，通过多层次语义对齐的交叉注意机制与部分关键词、场景属性和整体句子级别的多轨迹Mamba建模相结合，从而推进了跨模态token聚合。特别地，扫描轨迹是通过在每个时间步动态选择最近的视觉空间token来构建的，适用于部分关键词和场景属性级别。此外，我们设计了一种多层次语义对齐的交叉注意策略，从而能够更有效地聚合跨不同语义层次的空间和时间token。实验表明，RefAtomNet++建立了新的state-of-the-art结果。数据集和代码已在https://github.com/KPeng9510/refAVA2上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决指代表达式原子视频动作识别（RAVAR）任务中，现有方法在跨模态信息对齐和检索方面的不足。现有方法难以有效地将自然语言描述与视频中的人物动作关联起来，导致目标人物定位和细粒度动作识别的精度不高。

**核心思路**：论文的核心思路是利用多层次语义对齐的交叉注意机制和多轨迹Mamba建模，更有效地聚合跨模态的token信息。通过在部分关键词、场景属性和整体句子级别上进行建模，实现更精细的语义理解和更准确的动作识别。

**技术框架**：RefAtomNet++的整体框架包含以下几个主要模块：1) 特征提取模块，用于提取视频帧和文本描述的特征；2) 多轨迹Mamba建模模块，用于在部分关键词和场景属性级别上构建扫描轨迹，动态选择最近的视觉空间token；3) 多层次语义对齐的交叉注意模块，用于聚合跨不同语义层次的空间和时间token；4) 动作预测模块，用于预测目标人物的原子动作。

**关键创新**：RefAtomNet++的关键创新在于：1) 提出了多轨迹Mamba建模，能够动态地关注与关键词和场景属性相关的视觉区域；2) 设计了多层次语义对齐的交叉注意机制，能够更有效地聚合来自不同语义层次的信息，从而提升跨模态对齐的精度。

**关键设计**：在多轨迹Mamba建模中，通过动态选择最近的视觉空间token来构建扫描轨迹，使得模型能够关注与文本描述相关的视觉区域。在多层次语义对齐的交叉注意机制中，使用了不同的注意力权重来聚合来自不同语义层次的信息，从而实现更精细的语义理解。

## 📊 实验亮点

RefAtomNet++在RefAVA++数据集上取得了显著的性能提升，建立了新的state-of-the-art结果。相较于之前的RefAtomNet模型和其他基线方法，RefAtomNet++在目标人物定位和细粒度动作识别方面均有明显改善，验证了多层次语义对齐交叉注意机制和多轨迹Mamba建模的有效性。

## 🎯 应用场景

该研究成果可应用于智能监控、人机交互、视频内容分析等领域。例如，在智能监控中，可以利用该技术识别特定人员的异常行为；在人机交互中，可以实现更自然、更智能的交互方式；在视频内容分析中，可以自动识别视频中的人物动作，从而提高视频检索和理解的效率。

## 📄 摘要（原文）

> Referring Atomic Video Action Recognition (RAVAR) aims to recognize fine-grained, atomic-level actions of a specific person of interest conditioned on natural language descriptions. Distinct from conventional action recognition and detection tasks, RAVAR emphasizes precise language-guided action understanding, which is particularly critical for interactive human action analysis in complex multi-person scenarios. In this work, we extend our previously introduced RefAVA dataset to RefAVA++, which comprises >2.9 million frames and >75.1k annotated persons in total. We benchmark this dataset using baselines from multiple related domains, including atomic action localization, video question answering, and text-video retrieval, as well as our earlier model, RefAtomNet. Although RefAtomNet surpasses other baselines by incorporating agent attention to highlight salient features, its ability to align and retrieve cross-modal information remains limited, leading to suboptimal performance in localizing the target person and predicting fine-grained actions. To overcome the aforementioned limitations, we introduce RefAtomNet++, a novel framework that advances cross-modal token aggregation through a multi-hierarchical semantic-aligned cross-attention mechanism combined with multi-trajectory Mamba modeling at the partial-keyword, scene-attribute, and holistic-sentence levels. In particular, scanning trajectories are constructed by dynamically selecting the nearest visual spatial tokens at each timestep for both partial-keyword and scene-attribute levels. Moreover, we design a multi-hierarchical semantic-aligned cross-attention strategy, enabling more effective aggregation of spatial and temporal tokens across different semantic hierarchies. Experiments show that RefAtomNet++ establishes new state-of-the-art results. The dataset and code are released at https://github.com/KPeng9510/refAVA2.

