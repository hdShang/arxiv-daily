---
layout: default
title: Spatial Preference Rewarding for MLLMs Spatial Understanding
---

# Spatial Preference Rewarding for MLLMs Spatial Understanding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14374" target="_blank" class="toolbar-btn">arXiv: 2510.14374v1</a>
    <a href="https://arxiv.org/pdf/2510.14374.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14374v1" 
            onclick="toggleFavorite(this, '2510.14374v1', 'Spatial Preference Rewarding for MLLMs Spatial Understanding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Han Qiu, Peng Gao, Lewei Lu, Xiaoqin Zhang, Ling Shao, Shijian Lu

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/hanqiu-hq/SPR)

---

## 💡 一句话要点

**提出空间偏好奖励SPR，提升MLLM在细粒度空间理解上的能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `大型语言模型` `空间理解` `偏好学习` `目标定位`

## 📋 核心要点

1. 现有MLLM在细粒度空间感知上存在不足，难以生成精确区域描述或定位对象，且缺乏对模型响应的直接监督。
2. SPR通过奖励MLLM对精确对象定位的详细响应，惩罚模糊或不准确的响应，从而提升空间理解能力。
3. 实验表明，SPR在引用和定位基准测试中，以较小的训练开销有效提升了MLLM的空间理解能力。

## 📝 摘要（中文）

多模态大型语言模型(MLLMs)在空间理解方面展现出潜力，例如引用和定位对象描述。尽管如此，MLLMs在细粒度空间感知能力方面仍有不足，如生成详细的区域描述或精确定位对象。此外，它们常常无法满足用户对细粒度空间理解的需求。这个问题可能源于现有方法主要集中于调整MLLMs以建模预先标注的指令数据来注入空间知识，而缺乏对MLLMs实际响应的直接监督。我们通过空间偏好奖励(SPR)方法来解决这个问题，该方法通过奖励MLLMs对精确对象定位的详细响应，而不是模糊或不准确的响应，从而增强MLLMs的空间能力。SPR从MLLMs中随机选择图像区域和区域描述，引入语义和定位分数来全面评估MLLM生成的描述中的文本质量和定位质量。我们还使用更好的定位精度来改进MLLM描述，并将最佳得分的改进与最低得分的初始描述配对，以进行直接偏好优化，从而增强与视觉输入的细粒度对齐。在标准引用和定位基准上的大量实验表明，SPR以最小的训练开销有效地提高了MLLM的空间理解能力。

## 🔬 方法详解

**问题定义**：MLLM在细粒度空间理解方面存在不足，具体表现为无法生成详细的区域描述或精确定位对象，并且难以满足用户对细粒度空间理解的需求。现有方法主要依赖于预标注的指令数据来训练MLLM，缺乏对模型实际响应的直接监督，导致模型无法有效学习到细粒度的空间知识。

**核心思路**：SPR的核心思路是通过奖励机制来引导MLLM生成更精确、更符合用户期望的空间描述。具体来说，SPR会评估MLLM生成的描述的语义质量和定位质量，并根据评估结果对模型进行奖励或惩罚。通过这种方式，模型可以学习到如何生成更准确、更详细的空间描述，从而提升其细粒度空间理解能力。

**技术框架**：SPR方法主要包含以下几个阶段：1) 从MLLM中随机选择图像区域和区域描述；2) 引入语义和定位分数来评估MLLM生成的描述的文本质量和定位质量；3) 使用更好的定位精度来改进MLLM描述；4) 将最佳得分的改进与最低得分的初始描述配对，以进行直接偏好优化。整个框架通过不断地优化MLLM的响应，从而提升其空间理解能力。

**关键创新**：SPR的关键创新在于引入了空间偏好奖励机制，通过直接监督MLLM的响应来提升其细粒度空间理解能力。与现有方法相比，SPR不需要依赖大量的预标注数据，而是通过奖励机制来引导模型学习，从而降低了训练成本，并提高了模型的泛化能力。

**关键设计**：SPR的关键设计包括：1) 语义和定位分数的计算方法，用于评估MLLM生成的描述的质量；2) 改进MLLM描述的方法，用于提高描述的定位精度；3) 直接偏好优化算法，用于训练MLLM生成更符合用户期望的响应。具体的参数设置和损失函数等细节在论文中进行了详细描述。

## 📊 实验亮点

SPR在标准引用和定位基准测试中取得了显著的性能提升。实验结果表明，SPR能够有效地提高MLLM的空间理解能力，并且只需要最小的训练开销。具体的性能数据和对比基线在论文中进行了详细的展示，证明了SPR的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、智能监控、图像编辑等领域。例如，在机器人导航中，可以利用该技术使机器人能够更准确地理解人类的指令，从而更好地完成导航任务。在自动驾驶中，可以提高车辆对周围环境的感知能力，从而提高驾驶安全性。在智能监控中，可以实现对特定区域的精细化监控，从而提高监控效率。

## 📄 摘要（原文）

> Multimodal large language models~(MLLMs) have demonstrated promising spatial understanding capabilities, such as referencing and grounding object descriptions. Despite their successes, MLLMs still fall short in fine-grained spatial perception abilities, such as generating detailed region descriptions or accurately localizing objects. Additionally, they often fail to respond to the user's requirements for desired fine-grained spatial understanding. This issue might arise because existing approaches primarily focus on tuning MLLMs to model pre-annotated instruction data to inject spatial knowledge, without direct supervision of MLLMs' actual responses. We address this issue by SPR, a Spatial Preference Rewarding~(SPR) approach that enhances MLLMs' spatial capabilities by rewarding MLLMs' detailed responses with precise object localization over vague or inaccurate responses. With randomly selected image regions and region descriptions from MLLMs, SPR introduces semantic and localization scores to comprehensively evaluate the text quality and localization quality in MLLM-generated descriptions. We also refine the MLLM descriptions with better localization accuracy and pair the best-scored refinement with the initial descriptions of the lowest score for direct preference optimization, thereby enhancing fine-grained alignment with visual input. Extensive experiments over standard referring and grounding benchmarks show that SPR improves MLLM spatial understanding capabilities effectively with minimal overhead in training. Data and code will be released at https://github.com/hanqiu-hq/SPR

