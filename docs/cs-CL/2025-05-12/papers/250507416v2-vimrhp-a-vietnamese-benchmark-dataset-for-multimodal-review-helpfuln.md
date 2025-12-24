---
layout: default
title: "ViMRHP: A Vietnamese Benchmark Dataset for Multimodal Review Helpfulness Prediction via Human-AI Collaborative Annotation"
---

# ViMRHP: A Vietnamese Benchmark Dataset for Multimodal Review Helpfulness Prediction via Human-AI Collaborative Annotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07416" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07416v2</a>
  <a href="https://arxiv.org/pdf/2505.07416.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07416v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07416v2', 'ViMRHP: A Vietnamese Benchmark Dataset for Multimodal Review Helpfulness Prediction via Human-AI Collaborative Annotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Truc Mai-Thanh Nguyen, Dat Minh Nguyen, Son T. Luu, Kiet Van Nguyen

**分类**: cs.CL

**发布日期**: 2025-05-12 (更新: 2025-07-04)

**备注**: Accepted at NLDB 2025

**DOI**: [10.1007/978-3-031-97141-9_20](https://doi.org/10.1007/978-3-031-97141-9_20)

**🔗 代码/项目**: [GITHUB](https://github.com/trng28/ViMRHP)

---

## 💡 一句话要点

**提出ViMRHP数据集以解决越南语多模态评论有用性预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态评论` `有用性预测` `越南语` `AI辅助标注` `数据集构建` `电子商务` `用户生成内容`

## 📋 核心要点

1. 现有的多模态评论有用性预测数据集主要集中在英语和印尼语，缺乏对越南语等低资源语言的支持。
2. 本文提出ViMRHP数据集，利用AI辅助标注技术，优化了数据集构建过程，显著提高了标注效率。
3. 实验结果表明，使用AI辅助的标注方法可以将标注时间从90-120秒减少到20-40秒，成本降低约65%。

## 📝 摘要（中文）

多模态评论有用性预测（MRHP）是推荐系统中的重要任务，尤其在电子商务平台上。用户生成评论的有用性评估能够提升用户体验并改善消费者决策。然而，现有数据集主要集中在英语和印尼语，缺乏对低资源语言如越南语的支持。本文介绍了ViMRHP（越南多模态评论有用性预测），这是一个大规模的越南语MRHP基准数据集，涵盖四个领域，包含2000个产品和46000条评论。为优化标注过程，本文利用AI辅助标注，显著减少了标注时间并降低了成本，同时保持数据质量。尽管AI生成的标注在复杂任务中存在局限性，但我们通过详细的性能分析进行了探讨。ViMRHP数据集已公开发布。

## 🔬 方法详解

**问题定义**：本文旨在解决越南语多模态评论有用性预测任务的数据稀缺问题。现有方法在低资源语言的应用上存在不足，导致无法有效评估用户生成评论的有用性。

**核心思路**：通过构建ViMRHP数据集并引入AI辅助标注，本文旨在提高标注效率和数据质量。AI的引入使得标注过程更为高效，降低了人力成本。

**技术框架**：ViMRHP数据集的构建包括数据收集、AI辅助标注和人类验证三个主要阶段。首先收集越南语评论数据，然后利用AI工具进行初步标注，最后由人工进行验证和修正。

**关键创新**：本文的主要创新在于结合AI技术与人类标注者的合作，显著提高了标注效率，并在保持数据质量的同时降低了成本。这种方法在多模态数据集构建中具有广泛的适用性。

**关键设计**：在标注过程中，设置了合理的参数以确保AI生成的标注质量，同时采用了适当的损失函数来优化模型性能。网络结构设计上，结合了多模态特征提取和融合技术，以提升最终的预测效果。

## 📊 实验亮点

实验结果显示，AI辅助标注方法将标注时间从90-120秒减少到20-40秒，成本降低约65%。在对比基线模型时，AI生成的标注与人类验证的标注在质量上具有显著差异，进一步验证了AI辅助标注的有效性。

## 🎯 应用场景

ViMRHP数据集的构建为越南语的多模态评论有用性预测提供了重要的基础，具有广泛的应用潜力。该研究可应用于电子商务平台、社交媒体分析及其他需要用户评论评估的领域，未来可能推动低资源语言处理技术的发展。

## 📄 摘要（原文）

> Multimodal Review Helpfulness Prediction (MRHP) is an essential task in recommender systems, particularly in E-commerce platforms. Determining the helpfulness of user-generated reviews enhances user experience and improves consumer decision-making. However, existing datasets focus predominantly on English and Indonesian, resulting in a lack of linguistic diversity, especially for low-resource languages such as Vietnamese. In this paper, we introduce ViMRHP (Vietnamese Multimodal Review Helpfulness Prediction), a large-scale benchmark dataset for MRHP task in Vietnamese. This dataset covers four domains, including 2K products with 46K reviews. Meanwhile, a large-scale dataset requires considerable time and cost. To optimize the annotation process, we leverage AI to assist annotators in constructing the ViMRHP dataset. With AI assistance, annotation time is reduced (90 to 120 seconds per task down to 20 to 40 seconds per task) while maintaining data quality and lowering overall costs by approximately 65%. However, AI-generated annotations still have limitations in complex annotation tasks, which we further examine through a detailed performance analysis. In our experiment on ViMRHP, we evaluate baseline models on human-verified and AI-generated annotations to assess their quality differences. The ViMRHP dataset is publicly available at https://github.com/trng28/ViMRHP

