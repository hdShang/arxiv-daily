---
layout: default
title: FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14574</a>
  <a href="https://arxiv.org/pdf/2512.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14574" onclick="toggleFavorite(this, '2512.14574', 'FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mitsuki Watanabe, Sosuke Amano, Kiyoharu Aizawa, Yoko Yamakata

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FoodLogAthl-218：构建基于膳食管理应用采集的真实食物图像数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `食物图像分类` `膳食管理` `真实数据集` `增量学习` `上下文感知`

## 📋 核心要点

1. 现有食物图像数据集多为网络爬取，与用户真实膳食照片存在差异，影响膳食管理应用效果。
2. 提出FoodLogAthl-218数据集，直接从膳食管理应用收集用户真实膳食图像，更贴近实际应用场景。
3. 引入增量微调和上下文感知分类任务，更符合FoodLog应用特点，并使用LMM进行评估。

## 📝 摘要（中文）

本文提出了FoodLogAthl-218，一个基于膳食管理应用FoodLog Athl收集的真实食物图像数据集。该数据集包含218个食物类别的6925张图像，以及总计14349个边界框。每张图像都附带有丰富的元数据，包括用餐日期和时间、匿名用户ID以及膳食级别的上下文信息。与传统的依赖网络爬取图像的数据集不同，该数据集从用户提交的照片开始，然后进行标签标注，从而产生更大的类内多样性、膳食类型的自然频率分布以及未经滤镜处理的个人使用图像。除了标准的分类基准测试外，还引入了两个FoodLog特定的任务：（1）遵循用户日志时间流的增量微调协议，以及（2）上下文感知的分类任务，其中每张图像包含多个菜肴，模型必须利用整体膳食上下文对每个菜肴进行分类。使用大型多模态模型（LMM）评估了这些任务。该数据集已公开。

## 🔬 方法详解

**问题定义**：现有食物图像分类模型依赖的数据集通常通过网络爬取获得，这些图像与用户在膳食管理应用中拍摄的真实照片存在显著差异。这种差异导致模型在实际应用中的性能下降，无法有效减轻用户手动记录膳食的负担。因此，需要一个更贴近真实用户场景的食物图像数据集。

**核心思路**：该论文的核心思路是直接从膳食管理应用FoodLog Athl收集用户上传的真实膳食图像，并构建一个包含丰富元数据的数据集。这种方法避免了网络爬取图像与真实用户照片之间的差异，从而能够训练出更有效的食物图像分类模型。此外，论文还设计了针对FoodLog应用特点的特定任务，以更好地评估模型的性能。

**技术框架**：该论文主要关注数据集的构建和基准测试任务的设计。数据集构建过程包括：1) 从FoodLog Athl应用收集用户上传的膳食图像；2) 对图像进行标注，包括食物类别和边界框；3) 添加元数据，如用餐日期和时间、用户ID和膳食级别上下文信息。基准测试任务包括：1) 标准的食物图像分类任务；2) 增量微调任务，模拟用户日志的时间流；3) 上下文感知的分类任务，利用膳食上下文信息进行分类。

**关键创新**：该论文的关键创新在于数据集的构建方法。与传统的网络爬取数据集不同，FoodLogAthl-218直接从用户上传的真实膳食图像中构建，从而具有更高的类内多样性、更自然的膳食类型分布以及更真实的图像质量。此外，论文还提出了针对FoodLog应用特点的增量微调和上下文感知分类任务，更贴近实际应用场景。

**关键设计**：数据集包含218个食物类别，6925张图像和14349个边界框。增量微调任务按照用户日志的时间顺序进行微调，模拟用户使用应用的真实过程。上下文感知的分类任务需要模型利用膳食中其他菜肴的信息来辅助分类，例如，如果一张图片中包含米饭和味噌汤，则可以推断出该图片可能包含日式料理。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建的FoodLogAthl-218数据集具有真实性和多样性，更贴近实际应用场景。提出的增量微调和上下文感知分类任务更符合膳食管理应用的特点。实验结果表明，大型多模态模型（LMM）在该数据集上表现良好，为后续研究提供了有价值的参考。

## 🎯 应用场景

该研究成果可直接应用于膳食管理应用中，提升食物图像识别的准确率，减轻用户手动记录膳食的负担。此外，该数据集和基准测试任务也可用于评估和改进现有的食物图像分类模型，推动相关领域的研究进展。未来，可以进一步探索利用该数据集进行个性化膳食推荐和营养分析。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available atthis https URL.

