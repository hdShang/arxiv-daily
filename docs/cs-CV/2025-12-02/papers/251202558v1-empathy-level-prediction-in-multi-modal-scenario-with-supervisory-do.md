---
layout: default
title: Empathy Level Prediction in Multi-Modal Scenario with Supervisory Documentation Assistance
---

# Empathy Level Prediction in Multi-Modal Scenario with Supervisory Documentation Assistance

**arXiv**: [2512.02558v1](https://arxiv.org/abs/2512.02558) | [PDF](https://arxiv.org/pdf/2512.02558.pdf)

**作者**: Yufei Xiao, Shangfei Wang

---

## 💡 一句话要点

**提出多模态共情预测方法，结合监督文档辅助训练以提升性能。**

**关键词**: `多模态共情预测` `跨模态融合` `监督文档辅助训练` `特权信息利用` `Latent Dirichlet Allocation`

## 📋 核心要点

1. 核心问题：现有共情预测方法多依赖单一模态，忽略多模态处理和特权信息利用。
2. 方法要点：整合视频、音频和文本特征，通过跨模态融合预测共情标签，并引入监督文档作为训练特权信息。
3. 实验或效果：在多模态和对话共情数据集上优于现有方法，验证了方法的有效性。

## 📄 摘要（原文）

> Prevalent empathy prediction techniques primarily concentrate on a singular modality, typically textual, thus neglecting multi-modal processing capabilities. They also overlook the utilization of certain privileged information, which may encompass additional empathetic content. In response, we introduce an advanced multi-modal empathy prediction method integrating video, audio, and text information. The method comprises the Multi-Modal Empathy Prediction and Supervisory Documentation Assisted Training. We use pre-trained networks in the empathy prediction network to extract features from various modalities, followed by a cross-modal fusion. This process yields a multi-modal feature representation, which is employed to predict empathy labels. To enhance the extraction of text features, we incorporate supervisory documents as privileged information during the assisted training phase. Specifically, we apply the Latent Dirichlet Allocation model to identify potential topic distributions to constrain text features. These supervisory documents, created by supervisors, focus on the counseling topics and the counselor's display of empathy. Notably, this privileged information is only available during training and is not accessible during the prediction phase. Experimental results on the multi-modal and dialogue empathy datasets demonstrate that our approach is superior to the existing methods.

