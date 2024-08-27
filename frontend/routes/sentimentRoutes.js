import express from 'express';
import { renderHome, analyzeText } from '../controllers/sentimentController.js';

const router = express.Router();

router.get('/', renderHome);
router.post('/analyze', analyzeText);

export default router;
