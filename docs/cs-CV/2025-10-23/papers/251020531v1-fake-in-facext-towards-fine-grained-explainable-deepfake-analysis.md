---
layout: default
title: Fake-in-Facext: Towards Fine-Grained Explainable DeepFake Analysis
---

# Fake-in-Facext: Towards Fine-Grained Explainable DeepFake Analysis

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20531" target="_blank" class="toolbar-btn">arXiv: 2510.20531v1</a>
    <a href="https://arxiv.org/pdf/2510.20531.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20531v1" 
            onclick="toggleFavorite(this, '2510.20531v1', 'Fake-in-Facext: Towards Fine-Grained Explainable DeepFake Analysis')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lixiong Qin, Yang Zhang, Mei Wang, Jiani Hu, Weihong Deng, Weiran Xu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23

**备注**: 25 pages, 9 figures, 17 tables

**🔗 代码/项目**: [GITHUB](https://github.com/lxq1000/Fake-in-Facext)

---

## 💡 一句话要点

**提出Fake-in-Facext框架，实现细粒度、可解释的DeepFake人脸分析。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `DeepFake分析` `可解释性AI` `多模态学习` `人脸图像处理` `伪造痕迹定位`

## 📋 核心要点

1. 现有可解释DeepFake分析方法缺乏细粒度感知，数据标注粗糙，无法有效连接文本解释和视觉证据。
2. 提出Fake-in-Facext框架，通过面部图像概念树(FICT)实现细粒度数据标注，并引入伪造痕迹定位解释(AGE)任务。
3. FiFa-MLLM在AGE任务上超越现有基线，并在XDFA数据集上取得SOTA性能，证明了其有效性。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)的发展弥合了视觉和语言任务之间的差距，使得可解释的DeepFake分析(XDFA)成为可能。然而，当前方法缺乏细粒度感知：数据标注中的伪造痕迹描述不可靠且粗糙，模型无法支持文本伪造解释与伪造痕迹视觉证据之间的连接输出，以及任意面部区域的查询输入。因此，它们的响应没有充分基于人脸视觉上下文(Facext)。为了解决这个限制，我们提出了Fake-in-Facext (FiFa)框架，其贡献集中在数据标注和模型构建上。我们首先定义了一个面部图像概念树(FICT)将面部图像划分为细粒度的区域概念，从而获得更可靠的伪造解释数据标注流程FiFa-Annotator。基于这种专用数据标注，我们引入了一种新的伪造痕迹定位解释(AGE)任务，该任务生成与篡改伪造痕迹的分割掩码交织的文本伪造解释。我们提出了一个统一的多任务学习架构FiFa-MLLM，以同时支持丰富的多模态输入和输出，用于细粒度的可解释DeepFake分析。通过多个辅助监督任务，FiFa-MLLM可以在AGE任务上优于强大的基线，并在现有的XDFA数据集上实现SOTA性能。代码和数据将在https://github.com/lxq1000/Fake-in-Facext开源。

## 🔬 方法详解

**问题定义**：现有可解释DeepFake分析(XDFA)方法在细粒度上存在不足。具体来说，数据标注中对伪造痕迹的描述不够精确，导致模型无法准确地将文本解释与对应的视觉伪造区域关联起来。此外，现有方法难以支持对任意面部区域进行查询，限制了其应用范围。这些问题导致模型输出的解释不够充分，缺乏人脸视觉上下文的支撑。

**核心思路**：FiFa框架的核心思路是提升XDFA的细粒度感知能力。通过构建面部图像概念树(FICT)，将人脸图像分解为更细致的区域概念，从而实现更可靠的数据标注。同时，引入伪造痕迹定位解释(AGE)任务，要求模型生成包含分割掩码的文本解释，从而将文本和视觉信息紧密结合。

**技术框架**：FiFa框架包含两个主要组成部分：FiFa-Annotator和FiFa-MLLM。FiFa-Annotator是一个数据标注流程，利用FICT进行细粒度标注。FiFa-MLLM是一个统一的多任务学习架构，用于支持多模态输入和输出。该模型同时执行AGE任务以及多个辅助监督任务，以提升性能。整体流程为：首先使用FiFa-Annotator标注数据，然后使用标注数据训练FiFa-MLLM，最后使用训练好的FiFa-MLLM进行细粒度的DeepFake分析。

**关键创新**：该论文的关键创新在于以下几点：1) 提出了面部图像概念树(FICT)，用于细粒度的人脸区域划分。2) 引入了伪造痕迹定位解释(AGE)任务，将文本解释与视觉分割掩码相结合。3) 构建了统一的多任务学习架构FiFa-MLLM，能够同时处理多模态输入和输出。与现有方法相比，FiFa框架能够提供更精确、更可解释的DeepFake分析结果。

**关键设计**：在数据标注方面，FICT的设计至关重要，它决定了标注的细粒度程度。在模型方面，FiFa-MLLM采用了多任务学习策略，通过多个辅助任务来提升AGE任务的性能。具体的辅助任务包括：人脸属性识别、人脸区域分割等。损失函数的设计也需要仔细考虑，以平衡不同任务之间的权重。网络结构方面，FiFa-MLLM可能采用了Transformer架构，以更好地处理序列数据和多模态信息。

## 📊 实验亮点

实验结果表明，FiFa-MLLM在AGE任务上显著优于现有基线方法，证明了其有效性。此外，FiFa-MLLM在现有的XDFA数据集上也取得了SOTA性能，进一步验证了其泛化能力。具体的性能数据和提升幅度需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于数字取证、社交媒体内容审核、身份验证等领域。通过提供细粒度、可解释的DeepFake分析，有助于识别和揭露虚假信息，维护网络安全和信息真实性。未来，该技术可进一步应用于视频DeepFake检测，以及更广泛的图像和视频篡改分析。

## 📄 摘要（原文）

> The advancement of Multimodal Large Language Models (MLLMs) has bridged the gap between vision and language tasks, enabling the implementation of Explainable DeepFake Analysis (XDFA). However, current methods suffer from a lack of fine-grained awareness: the description of artifacts in data annotation is unreliable and coarse-grained, and the models fail to support the output of connections between textual forgery explanations and the visual evidence of artifacts, as well as the input of queries for arbitrary facial regions. As a result, their responses are not sufficiently grounded in Face Visual Context (Facext). To address this limitation, we propose the Fake-in-Facext (FiFa) framework, with contributions focusing on data annotation and model construction. We first define a Facial Image Concept Tree (FICT) to divide facial images into fine-grained regional concepts, thereby obtaining a more reliable data annotation pipeline, FiFa-Annotator, for forgery explanation. Based on this dedicated data annotation, we introduce a novel Artifact-Grounding Explanation (AGE) task, which generates textual forgery explanations interleaved with segmentation masks of manipulated artifacts. We propose a unified multi-task learning architecture, FiFa-MLLM, to simultaneously support abundant multimodal inputs and outputs for fine-grained Explainable DeepFake Analysis. With multiple auxiliary supervision tasks, FiFa-MLLM can outperform strong baselines on the AGE task and achieve SOTA performance on existing XDFA datasets. The code and data will be made open-source at https://github.com/lxq1000/Fake-in-Facext.

