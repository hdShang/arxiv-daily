---
layout: default
title: "FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications"
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14574" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14574v1</a>
  <a href="https://arxiv.org/pdf/2512.14574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14574v1', 'FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications')" title="添加到收藏夹">☆ 收藏</button>
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

**关键词**: `食物图像分类` `真实数据集` `膳食管理` `增量学习` `上下文感知`

## 📋 核心要点

1. 现有食物图像数据集多为网络爬取，与用户真实膳食照片存在差异，影响膳食管理应用的准确性。
2. FoodLogAthl-218数据集直接从膳食管理应用收集用户上传的真实食物照片，更贴近实际应用场景。
3. 论文提出了增量微调和上下文感知分类两个FoodLog特定任务，并使用大型多模态模型进行了评估。

## 📝 摘要（中文）

本文提出了FoodLogAthl-218，一个基于膳食管理应用FoodLog Athl收集的真实食物图像数据集。该数据集包含218个食物类别的6925张图像，共计14349个边界框。每张图像都附带有丰富的元数据，包括用餐日期和时间、匿名用户ID以及膳食级别的上下文信息。与传统的基于网络爬取的、以预定义类别为导向的数据集不同，FoodLogAthl-218的数据来源于用户提交的照片，之后再进行标注，从而实现了更大的类内多样性、更自然的膳食类型频率分布以及更随意、未经滤镜处理的图像。除了标准的分类基准测试外，本文还引入了两个FoodLog特定的任务：一个遵循用户日志时间流的增量微调协议，以及一个上下文感知的分类任务，其中每张图像包含多个菜肴，模型必须利用整体膳食上下文对每个菜肴进行分类。使用大型多模态模型（LMMs）对这些任务进行了评估。该数据集已公开发布。

## 🔬 方法详解

**问题定义**：现有食物图像分类模型训练依赖的数据集，大多是通过网络爬取得到的图像。这些图像通常质量较高、摆放精美，与用户在日常生活中使用膳食管理应用时随手拍摄的食物照片存在显著差异。这种差异导致模型在真实应用场景下的性能下降。因此，需要一个更贴近实际用户使用场景的食物图像数据集，以提升膳食管理应用的准确性和实用性。

**核心思路**：论文的核心思路是直接从膳食管理应用的用户上传数据中构建数据集。通过这种方式，可以获得更真实的食物图像，包括不同的光照条件、拍摄角度、食物摆放方式等。此外，由于数据来源于真实用户，因此数据集能够反映用户真实的饮食习惯和膳食结构，从而更好地支持膳食管理应用。

**技术框架**：FoodLogAthl-218数据集的构建流程主要包括以下几个步骤：1) 数据收集：从膳食管理应用FoodLog Athl收集用户上传的食物图像及其相关的元数据，如用餐时间、用户ID等。2) 数据标注：对收集到的图像进行标注，包括食物类别的标注和边界框的标注。3) 数据划分：将数据集划分为训练集、验证集和测试集，用于模型训练和评估。4) 任务设计：设计了标准的分类任务，以及两个FoodLog特定的任务：增量微调和上下文感知分类。

**关键创新**：该论文的关键创新在于数据集的构建方式。与传统的基于网络爬取的数据集不同，FoodLogAthl-218数据集直接来源于真实用户上传的图像，因此具有更高的真实性和代表性。此外，论文还针对该数据集设计了两个FoodLog特定的任务，更贴合实际应用场景。

**关键设计**：在数据集构建方面，论文注重保持数据的自然分布，避免人为干预。在任务设计方面，增量微调任务模拟了用户在使用膳食管理应用时，随着时间的推移，不断接触新的食物类别的场景。上下文感知分类任务则考虑了膳食的整体搭配，要求模型能够利用膳食上下文信息来提高分类准确率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14574v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建的FoodLogAthl-218数据集包含218个食物类别，共计6925张图像和14349个边界框，规模适中且数据质量高。论文还提出了增量微调和上下文感知分类两个FoodLog特定任务，为后续研究提供了新的benchmark。虽然论文中没有给出具体的性能数据，但使用大型多模态模型（LMMs）对这些任务进行了评估，验证了数据集的有效性。

## 🎯 应用场景

该研究成果可直接应用于膳食管理和健康饮食推荐等领域。通过使用FoodLogAthl-218数据集训练的食物图像分类模型，可以自动识别用户拍摄的食物照片，减少用户手动记录膳食的负担。此外，结合用户的膳食记录和健康数据，可以为用户提供个性化的饮食建议，帮助用户改善饮食习惯，达到健康管理的目的。未来，该数据集还可以用于开发更智能的膳食管理应用，例如自动计算膳食营养成分、评估膳食健康程度等。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

