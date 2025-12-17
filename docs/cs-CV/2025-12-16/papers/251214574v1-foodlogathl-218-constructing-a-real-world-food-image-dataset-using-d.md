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

**提出FoodLogAthl-218真实世界食物图像数据集，以解决基于网络爬取图像训练模型与实际用户餐照差异大的问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `食物图像分类` `真实世界数据集` `饮食管理应用` `上下文感知学习` `增量微调` `大型多模态模型` `边界框标注` `用户生成内容`

## 📋 核心要点

1. 现有食物图像数据集多基于网络爬取，与实际用户餐照差异大，限制了模型在真实饮食管理应用中的性能。
2. 论文提出FoodLogAthl-218数据集，通过收集用户提交的真实餐照并后加标签，增强类内多样性和自然分布。
3. 实验引入增量微调和上下文感知分类任务，使用大型多模态模型评估，验证了数据集在真实场景下的有效性。

## 📝 摘要（中文）

食物图像分类模型对饮食管理应用至关重要，能减轻手动记录餐食的负担。然而，大多数公开可用的训练数据集依赖于网络爬取的图像，这些图像常与用户真实世界餐照存在差异。本研究介绍了FoodLogAthl-218，一个从饮食管理应用FoodLog Athl收集的真实世界餐食记录构建的食物图像数据集。该数据集包含6,925张图像，覆盖218个食物类别，总计14,349个边界框。每张图像附有丰富元数据，如餐食日期和时间、匿名用户ID及餐食级上下文。与传统数据集不同，后者基于预定义类别集指导网络图像收集，而我们的数据始于用户提交的照片，随后才应用标签。这带来了更大的类内多样性、餐食类型的自然频率分布，以及用于个人而非公开分享的随意、未过滤图像。除了（1）标准分类基准，我们引入了两个FoodLog特定任务：（2）遵循用户日志时间流的增量微调协议，和（3）上下文感知分类任务，其中每张图像包含多道菜肴，模型必须利用整体餐食上下文对每道菜进行分类。我们使用大型多模态模型（LMMs）评估这些任务。数据集公开可用，地址为https://huggingface.co/datasets/FoodLog/FoodLogAthl-218。

## 🔬 方法详解

论文的核心方法是构建FoodLogAthl-218数据集，整体框架包括从饮食管理应用FoodLog Athl收集用户真实餐食图像，并添加边界框和元数据。关键技术创新点在于数据收集方式：不同于传统基于预定义类别的网络爬取，本数据集基于用户提交照片后加标签，从而捕捉更真实的类内多样性和自然频率分布。与现有方法的主要区别在于强调真实世界场景，包括多菜肴图像和上下文信息，支持增量学习和上下文感知任务，以模拟实际应用中的动态需求。

## 📊 实验亮点

实验结果显示，FoodLogAthl-218数据集包含6,925张图像和14,349个边界框，覆盖218个类别，具有高类内多样性和自然分布。使用大型多模态模型评估，在增量微调和上下文感知分类任务中表现出色，验证了数据集在真实场景下的实用性和提升潜力。

## 🎯 应用场景

该研究主要应用于饮食管理领域，如健康监测、营养分析和个性化膳食推荐。通过提供真实世界食物图像数据集，能提升分类模型在实际应用中的准确性和鲁棒性，支持智能饮食日志和健康管理工具的开发。

## 📄 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

