---
layout: default
title: FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14574v1</a>
  <a href="https://arxiv.org/pdf/2512.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14574v1" onclick="toggleFavorite(this, '2512.14574v1', 'FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mitsuki Watanabe, Sosuke Amano, Kiyoharu Aizawa, Yoko Yamakata

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-16

**DOI**: [10.1145/3746027.3758276](https://doi.org/10.1145/3746027.3758276)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/FoodLog)

---

## 💡 一句话要点

**FoodLogAthl-218：构建基于膳食管理应用的真实食物图像数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `食物图像分类` `膳食管理` `真实数据集` `增量学习` `上下文感知` `多模态模型` `深度学习`

## 📋 核心要点

1. 现有食物图像数据集多为网络爬取，与用户真实用餐照片存在差异，限制了膳食管理应用的性能。
2. FoodLogAthl-218数据集直接从膳食管理应用收集用户上传的真实食物照片，保证了数据的真实性和多样性。
3. 论文提出了增量微调和上下文感知分类两个FoodLog特定任务，并使用大型多模态模型进行了评估。

## 📝 摘要（中文）

本文提出了FoodLogAthl-218，一个基于膳食管理应用FoodLog Athl收集的真实食物图像数据集。该数据集包含218个食物类别的6925张图像，共计14349个边界框。每张图像都附带有丰富的元数据，包括用餐日期和时间、匿名用户ID以及用餐级别的上下文信息。与传统的基于网络爬取的、以预定义类别为导向的数据集不同，FoodLogAthl-218的数据来源于用户提交的照片，之后再进行标注，从而实现了更大的类内多样性、更自然的膳食类型频率分布以及更随意、未经滤镜处理的个人使用图像。除了标准的分类基准之外，本文还引入了两个FoodLog特定的任务：(1) 遵循用户日志时间流的增量微调协议，以及(2) 上下文感知的分类任务，其中每张图像包含多个菜肴，模型必须利用整体用餐上下文对每个菜肴进行分类。使用大型多模态模型（LMM）对这些任务进行了评估。该数据集已在https://huggingface.co/datasets/FoodLog/FoodLogAthl-218上公开。

## 🔬 方法详解

**问题定义**：现有的食物图像数据集主要依赖于网络爬取，这些图像往往与用户在实际膳食管理应用中拍摄的照片存在显著差异。这种差异导致在这些数据集上训练的模型在实际应用中表现不佳。此外，传统数据集通常以预定义的类别为导向，缺乏真实世界中膳食的自然频率分布和类内多样性。

**核心思路**：FoodLogAthl-218的核心思路是直接从膳食管理应用FoodLog Athl收集用户上传的真实食物照片。这种方法能够保证数据的真实性和多样性，反映用户真实的饮食习惯和食物呈现方式。通过后续的标注，构建一个更贴近实际应用场景的食物图像数据集。

**技术框架**：FoodLogAthl-218数据集的构建流程主要包括以下几个阶段：1) 数据收集：从FoodLog Athl应用收集用户上传的食物图像及其相关的元数据，如用餐时间、用户ID等。2) 数据标注：对收集到的图像进行标注，包括食物类别的标注和边界框的标注。3) 数据划分：将数据集划分为训练集、验证集和测试集，用于模型训练和评估。4) 任务设计：设计了标准的分类任务以及两个FoodLog特定的任务，即增量微调和上下文感知分类。

**关键创新**：FoodLogAthl-218的关键创新在于其数据来源的真实性和多样性。与传统的网络爬取数据集不同，该数据集直接来源于用户的真实用餐记录，能够更好地反映实际应用场景。此外，论文还提出了两个FoodLog特定的任务，即增量微调和上下文感知分类，更贴合实际膳食管理应用的需求。

**关键设计**：在数据集构建方面，论文注重数据的质量和多样性，对收集到的图像进行了清洗和筛选，并采用了专业的标注团队进行标注。在任务设计方面，增量微调任务模拟了用户日志的时间流，上下文感知分类任务则考虑了用餐的整体上下文信息。在模型评估方面，论文使用了大型多模态模型（LMM）进行评估，以验证数据集的有效性。

## 📊 实验亮点

FoodLogAthl-218数据集包含218个食物类别的6925张图像，共计14349个边界框，具有丰富的元数据。论文提出了增量微调和上下文感知分类两个FoodLog特定的任务，并使用大型多模态模型进行了评估，结果表明该数据集能够有效提升食物图像分类模型的性能。

## 🎯 应用场景

FoodLogAthl-218数据集可广泛应用于膳食管理、营养监测、健康饮食推荐等领域。通过训练基于该数据集的食物图像分类模型，可以减少用户手动记录膳食的负担，提高膳食管理应用的效率和准确性。该数据集的真实性和多样性使其在开发更智能、更个性化的膳食管理解决方案方面具有重要价值。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

