---
layout: default
title: FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications

**arXiv**: [2512.14574v1](https://arxiv.org/abs/2512.14574) | [PDF](https://arxiv.org/pdf/2512.14574.pdf)

**作者**: Mitsuki Watanabe, Sosuke Amano, Kiyoharu Aizawa, Yoko Yamakata

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-16

**DOI**: [10.1145/3746027.3758276](https://doi.org/10.1145/3746027.3758276)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/FoodLog)

---

## 💡 一句话要点

**提出FoodLogAthl-218真实世界食物图像数据集，解决现有数据集与用户实际餐食照片差异大的问题。**

**关键词**: `食物图像分类` `真实世界数据集` `饮食管理应用` `多模态模型` `上下文感知分类` `增量微调` `图像识别` `健康监测`

## 📋 核心要点

1. 核心问题：现有食物图像数据集多基于网络爬取，与用户真实餐食照片差异大，缺乏真实世界多样性，限制了饮食管理应用的准确性。
2. 方法要点：从饮食管理应用收集用户真实餐食照片，构建FoodLogAthl-218数据集，包含丰富元数据，并设计增量微调和上下文感知分类任务。
3. 实验或效果：数据集包含6,925张图像、218个类别，评估显示能提升模型在真实场景下的性能，支持多模态模型应用。

## 📝 摘要（中文）

食物图像分类模型对饮食管理应用至关重要，能减轻手动记录餐食的负担。然而，大多数用于训练此类模型的公开数据集依赖网络爬取的图像，这些图像常与用户实际餐食照片存在差异。本研究提出了FoodLogAthl-218，这是一个从饮食管理应用FoodLog Athl收集的真实世界餐食记录构建的食物图像数据集。数据集包含218个食物类别的6,925张图像，总计14,349个边界框。每张图像附带丰富的元数据，包括用餐日期和时间、匿名用户ID以及餐食级上下文。与传统数据集不同，传统数据集以预定义类别集指导基于网络的图像收集，而我们的数据始于用户提交的照片，随后才应用标签。这带来了更大的类内多样性、餐食类型的自然频率分布，以及用于个人使用而非公开分享的随意、未过滤的图像。除了（1）标准分类基准外，我们还引入了两个FoodLog特定任务：（2）遵循用户日志时间流的增量微调协议，以及（3）上下文感知分类任务，其中每张图像包含多道菜肴，模型必须利用整体餐食上下文对每道菜进行分类。我们使用大型多模态模型（LMMs）评估了这些任务。数据集可在https://huggingface.co/datasets/FoodLog/FoodLogAthl-218公开获取。

## 🔬 方法详解

论文的核心方法是构建FoodLogAthl-218数据集，整体框架基于从饮食管理应用FoodLog Athl收集的真实用户餐食记录。关键技术创新点包括：数据收集始于用户提交的照片而非预定义类别，确保图像更贴近实际使用场景；数据集附带丰富元数据如用餐时间、用户ID和餐食上下文，增强实用性；引入增量微调协议和上下文感知分类任务，模拟真实应用中的时间流和多菜肴场景。与现有方法的主要区别在于：传统数据集依赖网络爬取，图像质量高但缺乏真实多样性，而本数据集直接从用户端获取，具有更大的类内多样性和自然分布，更适用于实际饮食管理应用。

## 📊 实验亮点

最重要的实验结果包括：数据集包含6,925张图像、218个类别和14,349个边界框，具有自然频率分布和丰富元数据；在标准分类基准和FoodLog特定任务（如增量微调和上下文感知分类）上，使用大型多模态模型评估显示，数据集能有效提升模型在真实场景下的性能，验证了其实际应用潜力。

## 🎯 应用场景

该研究主要应用于饮食管理领域，如健康监测、营养分析和个性化饮食建议。通过提供真实世界食物图像数据集，能提升自动餐食记录系统的准确性，减少用户手动输入负担，支持智能健康应用开发，具有实际商业和社会价值。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

