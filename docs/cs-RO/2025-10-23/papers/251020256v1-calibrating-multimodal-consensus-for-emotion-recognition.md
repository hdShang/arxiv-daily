---
layout: default
title: Calibrating Multimodal Consensus for Emotion Recognition
---

# Calibrating Multimodal Consensus for Emotion Recognition

**arXiv**: [2510.20256v1](https://arxiv.org/abs/2510.20256) | [PDF](https://arxiv.org/pdf/2510.20256.pdf)

**作者**: Guowei Zhong, Junjie Li, Huaiyu Zhu, Ruohong Huan, Yun Pan

---

## 💡 一句话要点

**提出校准多模态共识模型以解决多模态情感识别中的语义不一致和文本主导问题**

**关键词**: `多模态情感识别` `语义不一致` `文本主导` `自监督学习` `多模态融合` `伪标签生成`

## 📋 核心要点

1. 核心问题：多模态情感识别中存在跨模态语义不一致和文本主导导致的准确率下降
2. 方法要点：引入伪标签生成模块进行自监督预训练，并使用参数无关融合模块和多模态共识路由器进行微调
3. 实验或效果：在多个数据集上性能达到或超越先进方法，并在语义不一致场景中表现突出

## 📄 摘要（原文）

> In recent years, Multimodal Emotion Recognition (MER) has made substantial
> progress. Nevertheless, most existing approaches neglect the semantic
> inconsistencies that may arise across modalities, such as conflicting emotional
> cues between text and visual inputs. Besides, current methods are often
> dominated by the text modality due to its strong representational capacity,
> which can compromise recognition accuracy. To address these challenges, we
> propose a model termed Calibrated Multimodal Consensus (CMC). CMC introduces a
> Pseudo Label Generation Module (PLGM) to produce pseudo unimodal labels,
> enabling unimodal pretraining in a self-supervised fashion. It then employs a
> Parameter-free Fusion Module (PFM) and a Multimodal Consensus Router (MCR) for
> multimodal finetuning, thereby mitigating text dominance and guiding the fusion
> process toward a more reliable consensus. Experimental results demonstrate that
> CMC achieves performance on par with or superior to state-of-the-art methods
> across four datasets, CH-SIMS, CH-SIMS v2, CMU-MOSI, and CMU-MOSEI, and
> exhibits notable advantages in scenarios with semantic inconsistencies on
> CH-SIMS and CH-SIMS v2. The implementation of this work is publicly accessible
> at https://github.com/gw-zhong/CMC.

